import time
import uuid
from datetime import datetime, timezone
import numpy as np
import pandas as pd
from typing import List, Dict, Any, Optional

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc,
    mean_squared_error, mean_absolute_error, r2_score
)
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier

from app.schemas.experiment import (
    TrainExperimentRequest,
    ExperimentResult,
    MetricsSummary,
    ConfusionMatrixData,
    ROCCurveData,
    ROCPoint,
    FeatureImportance,
    PreprocessingConfig
)
from app.services.dataset_service import load_dataset_dataframe
from app.core.database import get_database

# In-memory fallback if MongoDB is in mock/test mode
EXPERIMENTS_STORE: List[Dict[str, Any]] = []

def instantiate_model(model_type: str, hyperparameters: Dict[str, Any]):
    """Instantiates a scikit-learn estimator with sanitized hyperparameters."""
    hp = hyperparameters.copy()

    # Classification
    if model_type == "logistic_regression":
        C = float(hp.get("C", 1.0))
        max_iter = int(hp.get("max_iter", 200))
        solver = hp.get("solver", "lbfgs")
        return LogisticRegression(C=C, max_iter=max_iter, solver=solver, random_state=42)

    elif model_type == "random_forest_classifier":
        n_estimators = int(hp.get("n_estimators", 100))
        max_depth = int(hp.get("max_depth", 10)) if hp.get("max_depth") else None
        min_samples_split = int(hp.get("min_samples_split", 2))
        return RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            random_state=42
        )

    elif model_type == "svm_classifier":
        C = float(hp.get("C", 1.0))
        kernel = hp.get("kernel", "rbf")
        gamma = hp.get("gamma", "scale")
        return SVC(C=C, kernel=kernel, gamma=gamma, probability=True, random_state=42)

    elif model_type == "knn_classifier":
        n_neighbors = int(hp.get("n_neighbors", 5))
        weights = hp.get("weights", "uniform")
        metric = hp.get("metric", "minkowski")
        return KNeighborsClassifier(n_neighbors=n_neighbors, weights=weights, metric=metric)

    elif model_type == "decision_tree_classifier":
        max_depth = int(hp.get("max_depth", 5)) if hp.get("max_depth") else None
        criterion = hp.get("criterion", "gini")
        return DecisionTreeClassifier(max_depth=max_depth, criterion=criterion, random_state=42)

    # Regression
    elif model_type == "linear_regression":
        return LinearRegression()

    elif model_type == "ridge_regression":
        alpha = float(hp.get("alpha", 1.0))
        return Ridge(alpha=alpha, random_state=42)

    elif model_type == "lasso_regression":
        alpha = float(hp.get("alpha", 1.0))
        return Lasso(alpha=alpha, random_state=42)

    elif model_type == "random_forest_regressor":
        n_estimators = int(hp.get("n_estimators", 100))
        max_depth = int(hp.get("max_depth", 10)) if hp.get("max_depth") else None
        return RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)

    elif model_type == "knn_regressor":
        n_neighbors = int(hp.get("n_neighbors", 5))
        return KNeighborsRegressor(n_neighbors=n_neighbors)

    else:
        raise ValueError(f"Unsupported model type: {model_type}")


async def train_and_evaluate_experiment(
    req: TrainExperimentRequest,
    user_id: Optional[str] = "demo_user"
) -> ExperimentResult:
    # 1. Load dataset
    df, dataset_name, _, task_type, target_column = load_dataset_dataframe(req.dataset_id)
    if not target_column or target_column not in df.columns:
        raise ValueError(f"Dataset '{req.dataset_id}' has no valid target column.")

    # 2. Select Features
    if req.feature_selection and len(req.feature_selection) > 0:
        valid_features = [f for f in req.feature_selection if f in df.columns and f != target_column]
        if not valid_features:
            raise ValueError("No valid features selected.")
        X_raw = df[valid_features].copy()
    else:
        X_raw = df.drop(columns=[target_column]).copy()
        valid_features = list(X_raw.columns)

    y_raw = df[target_column].copy()

    # Preprocessing: Only keep numeric features for simplicity and reliability
    numeric_feature_cols = [c for c in X_raw.columns if pd.api.types.is_numeric_dtype(X_raw[c])]
    if not numeric_feature_cols:
        raise ValueError("Selected features contain no numeric columns.")
    X_mat = X_raw[numeric_feature_cols].copy()

    # 3. Imputation
    if req.preprocessing.imputation == "mean":
        imputer = SimpleImputer(strategy="mean")
        X_mat = imputer.fit_transform(X_mat)
    elif req.preprocessing.imputation == "median":
        imputer = SimpleImputer(strategy="median")
        X_mat = imputer.fit_transform(X_mat)
    elif req.preprocessing.imputation == "drop":
        # Drop rows with NaN
        valid_idx = X_raw[numeric_feature_cols].dropna().index
        X_mat = X_raw.loc[valid_idx, numeric_feature_cols].values
        y_raw = y_raw.loc[valid_idx]
    else:
        # Default fallback fillna
        X_mat = X_mat.fillna(0.0).values

    # Encode Target if classification
    target_labels = None
    if req.task_type == "classification":
        le = LabelEncoder()
        y_vec = le.fit_transform(y_raw.astype(str))
        target_labels = [str(cls) for cls in le.classes_]
    else:
        y_vec = pd.to_numeric(y_raw, errors="coerce").fillna(0.0).values

    # 4. Scaling
    if req.preprocessing.scaling == "standard":
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_mat)
    elif req.preprocessing.scaling == "minmax":
        scaler = MinMaxScaler()
        X_scaled = scaler.fit_transform(X_mat)
    elif req.preprocessing.scaling == "robust":
        scaler = RobustScaler()
        X_scaled = scaler.fit_transform(X_mat)
    else:
        X_scaled = X_mat

    # 5. Train / Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled,
        y_vec,
        test_size=req.preprocessing.test_size,
        random_state=req.preprocessing.random_state
    )

    # 6. Fit Model & Benchmark time
    model = instantiate_model(req.model_type, req.hyperparameters)
    start_time = time.perf_counter()
    model.fit(X_train, y_train)
    training_time_ms = round((time.perf_counter() - start_time) * 1000.0, 2)

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # 7. Metrics calculation
    confusion_mat_data = None
    roc_curve_data = None

    if req.task_type == "classification":
        acc = float(accuracy_score(y_test, y_test_pred))
        prec = float(precision_score(y_test, y_test_pred, average="weighted", zero_division=0))
        rec = float(recall_score(y_test, y_test_pred, average="weighted", zero_division=0))
        f1 = float(f1_score(y_test, y_test_pred, average="weighted", zero_division=0))
        train_acc = float(accuracy_score(y_train, y_train_pred))

        metrics = MetricsSummary(
            accuracy=round(acc, 4),
            precision=round(prec, 4),
            recall=round(rec, 4),
            f1_score=round(f1, 4),
            train_score=round(train_acc, 4),
            test_score=round(acc, 4),
            training_time_ms=training_time_ms
        )

        # Confusion matrix
        cm = confusion_matrix(y_test, y_test_pred)
        confusion_mat_data = ConfusionMatrixData(
            labels=target_labels if target_labels else [str(i) for i in range(len(cm))],
            matrix=cm.tolist()
        )

        # ROC Curve for binary classification
        if len(np.unique(y_vec)) == 2:
            try:
                if hasattr(model, "predict_proba"):
                    y_prob = model.predict_proba(X_test)[:, 1]
                elif hasattr(model, "decision_function"):
                    y_prob = model.decision_function(X_test)
                else:
                    y_prob = y_test_pred

                fpr, tpr, _ = roc_curve(y_test, y_prob)
                roc_auc = float(auc(fpr, tpr))
                
                # Sample ROC points down to at most 30 points
                sample_indices = np.linspace(0, len(fpr) - 1, num=min(30, len(fpr)), dtype=int)
                roc_points = [
                    ROCPoint(fpr=round(float(fpr[i]), 4), tpr=round(float(tpr[i]), 4))
                    for i in sample_indices
                ]
                roc_curve_data = ROCCurveData(points=roc_points, auc=round(roc_auc, 4))
            except Exception:
                roc_curve_data = None

    else: # Regression
        mse = float(mean_squared_error(y_test, y_test_pred))
        rmse = float(np.sqrt(mse))
        mae = float(mean_absolute_error(y_test, y_test_pred))
        r2 = float(r2_score(y_test, y_test_pred))
        train_r2 = float(r2_score(y_train, y_train_pred))

        metrics = MetricsSummary(
            mse=round(mse, 4),
            rmse=round(rmse, 4),
            mae=round(mae, 4),
            r2_score=round(r2, 4),
            train_score=round(train_r2, 4),
            test_score=round(r2, 4),
            training_time_ms=training_time_ms
        )

    # 8. Feature Importances
    feature_importances: List[FeatureImportance] = []
    if hasattr(model, "feature_importances_"):
        fi_vals = model.feature_importances_
        for feat, imp in zip(numeric_feature_cols, fi_vals):
            feature_importances.append(FeatureImportance(feature=feat, importance=round(float(imp), 4)))
    elif hasattr(model, "coef_"):
        coefs = model.coef_
        if coefs.ndim > 1:
            coefs = np.mean(np.abs(coefs), axis=0)
        else:
            coefs = np.abs(coefs)
        total_coef = np.sum(coefs) if np.sum(coefs) > 0 else 1.0
        normalized = coefs / total_coef
        for feat, imp in zip(numeric_feature_cols, normalized):
            feature_importances.append(FeatureImportance(feature=feat, importance=round(float(imp), 4)))

    feature_importances.sort(key=lambda x: x.importance, reverse=True)

    exp_id = str(uuid.uuid4())[:8]
    exp_name = req.experiment_name or f"{req.model_type.replace('_', ' ').title()} on {dataset_name}"

    result = ExperimentResult(
        id=exp_id,
        user_id=user_id,
        experiment_name=exp_name,
        dataset_id=req.dataset_id,
        model_type=req.model_type,
        task_type=req.task_type,
        hyperparameters=req.hyperparameters,
        preprocessing=req.preprocessing,
        metrics=metrics,
        confusion_matrix=confusion_mat_data,
        roc_curve=roc_curve_data,
        feature_importances=feature_importances,
        created_at=datetime.now(timezone.utc).isoformat()
    )

    # Persist to DB or Memory
    try:
        db = get_database()
        await db.experiments.insert_one(result.model_dump())
    except Exception:
        EXPERIMENTS_STORE.insert(0, result.model_dump())

    return result


async def get_user_experiments(user_id: Optional[str] = None) -> List[ExperimentResult]:
    try:
        db = get_database()
        cursor = db.experiments.find({}).sort("created_at", -1).limit(50)
        docs = await cursor.to_list(length=50)
        if docs:
            return [ExperimentResult(**d) for d in docs]
    except Exception:
        pass
    
    return [ExperimentResult(**d) for d in EXPERIMENTS_STORE]


async def compare_experiments(experiment_ids: List[str]) -> List[ExperimentResult]:
    all_exps = await get_user_experiments()
    id_map = {e.id: e for e in all_exps}
    return [id_map[eid] for eid in experiment_ids if eid in id_map]
