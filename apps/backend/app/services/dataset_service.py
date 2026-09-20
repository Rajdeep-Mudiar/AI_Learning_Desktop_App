import io
import numpy as np
import pandas as pd
from typing import List, Dict, Any, Optional, Tuple
from sklearn import datasets as sk_datasets
from app.schemas.dataset import (
    ColumnSummary,
    CorrelationMatrix,
    DiagnosticWarning,
    DatasetListItem,
    DatasetProfileResponse
)

# In-memory registry of custom user datasets
CUSTOM_DATASETS_STORE: Dict[str, Dict[str, Any]] = {}

BUILTIN_CATALOG = [
    {
        "id": "iris",
        "name": "Iris Flower Classification",
        "description": "Fisher's classic dataset with 3 flower species and 4 botanical morphological features.",
        "task_type": "classification",
        "tags": ["Classification", "Multiclass", "Beginner", "Botany"]
    },
    {
        "id": "wine",
        "name": "Wine Recognition",
        "description": "Chemical analysis of wines grown in the same region in Italy derived from three different cultivars.",
        "task_type": "classification",
        "tags": ["Classification", "Multiclass", "Chemistry", "Medium"]
    },
    {
        "id": "breast_cancer",
        "name": "Breast Cancer Diagnostic",
        "description": "Diagnostic dataset with 30 computed nuclear features from fine needle aspirate (FNA) of breast masses.",
        "task_type": "classification",
        "tags": ["Classification", "Binary", "Medical", "High-Dimensional"]
    },
    {
        "id": "california_housing",
        "name": "California Housing Prices",
        "description": "Median house values for California districts from 1990 census with 8 demographic and geographical predictors.",
        "task_type": "regression",
        "tags": ["Regression", "Continuous", "Real Estate", "Benchmark"]
    },
    {
        "id": "diabetes",
        "name": "Diabetes Disease Progression",
        "description": "Ten baseline variables, age, sex, BMI, average blood pressure, and six blood serum measurements of 442 diabetes patients.",
        "task_type": "regression",
        "tags": ["Regression", "Healthcare", "Standardized"]
    }
]

def load_dataset_dataframe(dataset_id: str) -> Tuple[pd.DataFrame, str, str, str, Optional[str]]:
    """
    Loads raw dataframe, returns (df, name, description, task_type, target_column)
    """
    if dataset_id in CUSTOM_DATASETS_STORE:
        item = CUSTOM_DATASETS_STORE[dataset_id]
        return item["df"], item["name"], item["description"], item["task_type"], item["target_column"]

    if dataset_id == "iris":
        data = sk_datasets.load_iris(as_frame=True)
        df = data.frame.copy()
        target_name = "species"
        df[target_name] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})
        df = df.drop(columns=["target"])
        return df, "Iris Flower Classification", "Fisher's classic dataset with 3 flower species.", "classification", target_name

    elif dataset_id == "wine":
        data = sk_datasets.load_wine(as_frame=True)
        df = data.frame.copy()
        target_name = "cultivar"
        df[target_name] = df["target"].map({0: "class_0", 1: "class_1", 2: "class_2"})
        df = df.drop(columns=["target"])
        return df, "Wine Recognition", "Chemical analysis of wines grown in Italy.", "classification", target_name

    elif dataset_id == "breast_cancer":
        data = sk_datasets.load_breast_cancer(as_frame=True)
        df = data.frame.copy()
        target_name = "diagnosis"
        df[target_name] = df["target"].map({0: "malignant", 1: "benign"})
        df = df.drop(columns=["target"])
        return df, "Breast Cancer Diagnostic", "30 computed nuclear features of breast masses.", "classification", target_name

    elif dataset_id == "california_housing":
        data = sk_datasets.fetch_california_housing(as_frame=True)
        df = data.frame.head(1000).copy() # sample 1000 for fast interactive client responsiveness
        target_name = "MedHouseVal"
        return df, "California Housing Prices", "Median house values for California districts (1000 sample).", "regression", target_name

    elif dataset_id == "diabetes":
        data = sk_datasets.load_diabetes(as_frame=True)
        df = data.frame.copy()
        target_name = "target"
        return df, "Diabetes Disease Progression", "10 baseline patient variables and progression measure.", "regression", target_name

    else:
        raise ValueError(f"Unknown dataset '{dataset_id}'")


def profile_dataframe(
    dataset_id: str,
    df: pd.DataFrame,
    name: str,
    description: str,
    task_type: str,
    target_column: Optional[str]
) -> DatasetProfileResponse:
    columns_summary: List[ColumnSummary] = []
    diagnostic_warnings: List[DiagnosticWarning] = []
    
    # Analyze columns
    numeric_cols = []
    for col in df.columns:
        series = df[col]
        count = int(series.count())
        missing_count = int(series.isnull().sum())
        missing_ratio = float(missing_count / len(df)) if len(df) > 0 else 0.0
        unique_count = int(series.nunique())
        sample_vals = [x if pd.notnull(x) else None for x in series.dropna().head(5).tolist()]

        if pd.api.types.is_numeric_dtype(series):
            numeric_cols.append(col)
            mean_val = float(series.mean()) if count > 0 else None
            std_val = float(series.std()) if count > 1 else None
            min_val = float(series.min()) if count > 0 else None
            q25_val = float(series.quantile(0.25)) if count > 0 else None
            med_val = float(series.median()) if count > 0 else None
            q75_val = float(series.quantile(0.75)) if count > 0 else None
            max_val = float(series.max()) if count > 0 else None
            try:
                skew_val = float(series.skew()) if count > 2 and std_val and std_val > 0 else None
            except Exception:
                skew_val = None

            if skew_val is not None and abs(skew_val) > 2.0:
                diagnostic_warnings.append(DiagnosticWarning(
                    severity="warning",
                    title=f"High Skewness in '{col}'",
                    description=f"Column '{col}' shows substantial skewness ({round(skew_val, 2)}).",
                    recommendation="Consider applying a logarithmic, square-root, or Box-Cox transformation.",
                    affected_columns=[col]
                ))

            columns_summary.append(ColumnSummary(
                name=col,
                data_type="numeric",
                count=count,
                missing_count=missing_count,
                missing_ratio=round(missing_ratio, 4),
                mean=round(mean_val, 4) if mean_val is not None else None,
                std=round(std_val, 4) if std_val is not None else None,
                min=round(min_val, 4) if min_val is not None else None,
                q25=round(q25_val, 4) if q25_val is not None else None,
                median=round(med_val, 4) if med_val is not None else None,
                q75=round(q75_val, 4) if q75_val is not None else None,
                max=round(max_val, 4) if max_val is not None else None,
                unique_count=unique_count,
                sample_values=sample_vals,
                skewness=round(skew_val, 3) if skew_val is not None else None
            ))
        else:
            columns_summary.append(ColumnSummary(
                name=col,
                data_type="categorical" if unique_count < 50 else "text",
                count=count,
                missing_count=missing_count,
                missing_ratio=round(missing_ratio, 4),
                unique_count=unique_count,
                sample_values=sample_vals
            ))

        if missing_ratio > 0.05:
            diagnostic_warnings.append(DiagnosticWarning(
                severity="warning" if missing_ratio < 0.3 else "critical",
                title=f"Missing Values in '{col}'",
                description=f"{round(missing_ratio * 100, 1)}% of values in '{col}' are missing.",
                recommendation="Apply median/mean imputation or consider dropping if > 50% missing.",
                affected_columns=[col]
            ))

    # Correlation Matrix
    corr_matrix_obj = None
    if len(numeric_cols) >= 2:
        num_df = df[numeric_cols].dropna()
        if len(num_df) > 2:
            corr_df = num_df.corr().fillna(0.0)
            corr_feats = list(corr_df.columns)
            corr_mat = corr_df.round(3).values.tolist()
            corr_matrix_obj = CorrelationMatrix(features=corr_feats, matrix=corr_mat)

            # Check for high multicollinearity
            high_corr_pairs = []
            for i in range(len(corr_feats)):
                for j in range(i + 1, len(corr_feats)):
                    c_val = corr_mat[i][j]
                    if abs(c_val) >= 0.85:
                        high_corr_pairs.append((corr_feats[i], corr_feats[j], c_val))

            if high_corr_pairs:
                desc = ", ".join([f"{p[0]} & {p[1]} (r={p[2]})" for p in high_corr_pairs[:3]])
                diagnostic_warnings.append(DiagnosticWarning(
                    severity="warning",
                    title="High Multicollinearity Detected",
                    description=f"Strong correlation between feature pairs: {desc}.",
                    recommendation="Consider feature selection, PCA dimensionality reduction, or L2 (Ridge) regularization to stabilize coefficients.",
                    affected_columns=[p[0] for p in high_corr_pairs] + [p[1] for p in high_corr_pairs]
                ))

    # Class distribution if classification
    class_distribution = None
    if task_type == "classification" and target_column and target_column in df.columns:
        counts = df[target_column].value_counts().to_dict()
        class_distribution = {str(k): int(v) for k, v in counts.items()}
        
        # Check class imbalance
        if len(counts) >= 2:
            max_c = max(counts.values())
            min_c = min(counts.values())
            if min_c > 0 and (max_c / min_c) >= 3.0:
                diagnostic_warnings.append(DiagnosticWarning(
                    severity="critical" if (max_c / min_c) >= 5.0 else "warning",
                    title="Severe Class Imbalance Detected",
                    description=f"Dominant class has {max_c} samples versus minority class with {min_c} samples (ratio {round(max_c/min_c, 1)}:1).",
                    recommendation="Evaluate model using Balanced Accuracy, F1-Score, or PR-AUC rather than raw accuracy. Use class_weight='balanced' or SMOTE oversampling.",
                    affected_columns=[target_column]
                ))

    # Sample rows (top 20)
    clean_sample_df = df.head(20).replace({np.nan: None})
    sample_rows = clean_sample_df.to_dict(orient="records")

    features = [c for c in df.columns if c != target_column]

    return DatasetProfileResponse(
        id=dataset_id,
        name=name,
        description=description,
        task_type=task_type,
        num_rows=len(df),
        num_columns=len(df.columns),
        target_column=target_column,
        features=features,
        columns_summary=columns_summary,
        correlation_matrix=corr_matrix_obj,
        diagnostic_warnings=diagnostic_warnings,
        sample_rows=sample_rows,
        class_distribution=class_distribution
    )


def list_all_datasets() -> List[DatasetListItem]:
    items: List[DatasetListItem] = []
    for meta in BUILTIN_CATALOG:
        df, name, desc, task_type, target = load_dataset_dataframe(meta["id"])
        items.append(DatasetListItem(
            id=meta["id"],
            name=name,
            description=desc,
            task_type=task_type,
            num_rows=len(df),
            num_columns=len(df.columns),
            target_column=target,
            tags=meta["tags"]
        ))

    for cust_id, cust in CUSTOM_DATASETS_STORE.items():
        df = cust["df"]
        items.append(DatasetListItem(
            id=cust_id,
            name=cust["name"],
            description=cust["description"],
            task_type=cust["task_type"],
            num_rows=len(df),
            num_columns=len(df.columns),
            target_column=cust["target_column"],
            tags=["Custom", "Uploaded"]
        ))
    return items


def register_custom_csv_dataset(
    name: str,
    description: Optional[str],
    task_type: str,
    target_column: Optional[str],
    csv_content: str
) -> DatasetProfileResponse:
    df = pd.read_csv(io.StringIO(csv_content))
    if len(df) == 0:
        raise ValueError("CSV is empty or could not be parsed.")
    
    if target_column and target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' does not exist in CSV headers.")
    elif not target_column:
        target_column = df.columns[-1]

    dataset_id = f"custom_{abs(hash(name + str(len(df)))) % 100000}"
    CUSTOM_DATASETS_STORE[dataset_id] = {
        "df": df,
        "name": name,
        "description": description or "User uploaded dataset",
        "task_type": task_type,
        "target_column": target_column
    }
    return profile_dataframe(dataset_id, df, name, description or "User uploaded dataset", task_type, target_column)
