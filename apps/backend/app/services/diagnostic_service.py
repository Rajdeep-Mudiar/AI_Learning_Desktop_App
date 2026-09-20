from typing import List, Optional
from fastapi import HTTPException, status
from app.schemas.diagnostic import (
    DiagnosticScenarioSummary, DiagnosticScenarioDetail,
    DiagnosticSubmissionRequest, DiagnosticSubmissionResponse
)

DIAGNOSTIC_SCENARIOS = [
    {
        "id": "scenario-data-leakage",
        "title": "The Suspicious 99.8% Test Accuracy",
        "category": "Data Leakage",
        "difficulty": "Intermediate",
        "description": "A student engineer built a medical diagnosis classifier. The test accuracy is 99.8% in the notebook, but upon deploying to new hospital patients, accuracy drops to 52%. Inspect the pipeline to locate the bug.",
        "symptoms": [
            "Notebook validation score is 99.8%",
            "Production score drops to random chance (52%)",
            "Target feature: 'has_diabetes'"
        ],
        "code_snippet": (
            "import pandas as pd\n"
            "from sklearn.preprocessing import StandardScaler\n"
            "from sklearn.model_selection import train_test_split\n"
            "from sklearn.linear_model import LogisticRegression\n\n"
            "# 1. Load full dataset\n"
            "df = pd.read_csv('patient_records.csv')\n"
            "X = df.drop(columns=['patient_id', 'has_diabetes'])\n"
            "y = df['has_diabetes']\n\n"
            "# 2. Normalize entire dataset\n"
            "scaler = StandardScaler()\n"
            "X_scaled = scaler.fit_transform(X) # <-- Look closely here!\n\n"
            "# 3. Split into train and test\n"
            "X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)\n\n"
            "# 4. Fit model\n"
            "model = LogisticRegression()\n"
            "model.fit(X_train, y_train)\n"
            "print('Test Accuracy:', model.score(X_test, y_test))\n"
        ),
        "metrics_log": {
            "Train Accuracy": "0.999",
            "Test Accuracy": "0.998",
            "Production Accuracy": "0.521",
            "Feature Count": 14
        },
        "hints": [
            "Hint 1: Check when the StandardScaler computes its mean and variance.",
            "Hint 2: Does the scaler have access to information from the test split before the split occurs?",
            "Hint 3: Preprocessing transformations must only be fit on the training partition!"
        ],
        "options": [
            "The Logistic Regression C regularizer is too large",
            "Preprocessing Data Leakage: StandardScaler fit_transform was executed on the full dataset before splitting",
            "The test_size parameter of 0.2 is too small",
            "patient_id was not dropped from the dataframe"
        ],
        "correct_option": 1,
        "explanation": "Data Leakage occurs when information outside the training dataset is used to fit models or transformers. By calling `scaler.fit_transform(X)` before `train_test_split`, the test set's mean and variance leaked into the scaling parameters.",
        "fix_code_snippet": (
            "# Correct Workflow:\n"
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n"
            "scaler = StandardScaler()\n"
            "X_train_scaled = scaler.fit_transform(X_train)\n"
            "X_test_scaled = scaler.transform(X_test) # Fit ONLY on training data!"
        ),
        "concept_mastered": "Data Leakage & Preprocessing Partitioning",
        "xp_reward": 50
    },
    {
        "id": "scenario-overfitting-polynomial",
        "title": "The Wild Rollercoaster Fit",
        "category": "Overfitting & Complexity",
        "difficulty": "Beginner",
        "description": "With only 15 training points, the model achieves 0.0 MSE loss on training data, but produces absurd predictions (e.g. negative house prices) on new inputs.",
        "symptoms": [
            "Training MSE: 0.000",
            "Test MSE: 4892.45",
            "Severe oscillations between adjacent data points"
        ],
        "code_snippet": (
            "from sklearn.preprocessing import PolynomialFeatures\n"
            "from sklearn.linear_model import LinearRegression\n\n"
            "# 15 small data points\n"
            "poly = PolynomialFeatures(degree=14)\n"
            "X_poly = poly.fit_transform(X_train)\n\n"
            "model = LinearRegression()\n"
            "model.fit(X_poly, y_train)"
        ),
        "metrics_log": {
            "Training Samples": 15,
            "Polynomial Degree": 14,
            "Train Loss (MSE)": "0.000",
            "Test Loss (MSE)": "4892.45"
        },
        "hints": [
            "Hint 1: How many polynomial features are generated for a degree-14 transformation?",
            "Hint 2: When number of parameters equals or exceeds the number of data points, what happens to variance?"
        ],
        "options": [
            "The model is suffering from severe High Bias (Underfitting)",
            "The model has too much capacity (High Variance / Overfitting) due to degree=14 polynomial on only 15 samples",
            "LinearRegression cannot handle floating point numbers",
            "The random seed was not set"
        ],
        "correct_option": 1,
        "explanation": "A degree-14 polynomial has 15 parameters, exactly matching the 15 training points. It interpolates every point perfectly (including noise) but has massive generalization error.",
        "fix_code_snippet": (
            "# Use lower polynomial degree or Ridge/Lasso regularization:\n"
            "poly = PolynomialFeatures(degree=2)\n"
            "model = Ridge(alpha=1.0)"
        ),
        "concept_mastered": "Bias-Variance Tradeoff & Model Capacity",
        "xp_reward": 50
    },
    {
        "id": "scenario-class-imbalance",
        "title": "The Fraud Detection Mirage",
        "category": "Class Imbalance & Metrics",
        "difficulty": "Beginner",
        "description": "A credit card fraud model reports 99.2% accuracy. Management is celebrating, but the fraud department reports that zero fraudulent transactions are being blocked.",
        "symptoms": [
            "Reported Accuracy: 99.2%",
            "Recall on Fraud Class: 0.000",
            "Confusion Matrix shows zero true positive fraud predictions"
        ],
        "code_snippet": (
            "# Fraud is 0.8% of the dataset (992 normal, 8 fraud transactions)\n"
            "model.fit(X_train, y_train)\n"
            "y_pred = model.predict(X_test)\n"
            "print('Accuracy:', accuracy_score(y_test, y_pred))\n"
            "# Output: 0.992"
        ),
        "metrics_log": {
            "Total Test Samples": 1000,
            "Legitimate Transactions": 992,
            "Fraudulent Transactions": 8,
            "Model Predicted Fraud": 0
        },
        "hints": [
            "Hint 1: If a model simply outputs 'Legitimate' for every single transaction, what would its accuracy be?",
            "Hint 2: Look at Precision, Recall, and F1-Score instead of raw Accuracy."
        ],
        "options": [
            "Accuracy is misleading due to severe Class Imbalance; the model learned a trivial majority-class classifier",
            "The dataset has missing NaN values",
            "The model learning rate is too small",
            "Decision trees cannot perform binary classification"
        ],
        "correct_option": 0,
        "explanation": "On an imbalanced dataset (99.2% negative, 0.8% positive), a dummy classifier predicting class 0 always achieves 99.2% accuracy while finding zero fraud cases. Use Precision-Recall AUC, F1-Score, and class weighting (`class_weight='balanced'`).",
        "fix_code_snippet": (
            "# Use class-weighted loss and evaluate Precision/Recall:\n"
            "model = LogisticRegression(class_weight='balanced')\n"
            "print(classification_report(y_test, y_pred))"
        ),
        "concept_mastered": "Class Imbalance & Metric Selection (F1 / Recall vs Accuracy)",
        "xp_reward": 50
    }
]

class DiagnosticService:
    @staticmethod
    def list_scenarios() -> List[DiagnosticScenarioSummary]:
        return [
            DiagnosticScenarioSummary(
                id=s["id"],
                title=s["title"],
                category=s["category"],
                difficulty=s["difficulty"],
                description=s["description"],
                symptoms=s["symptoms"],
                xp_reward=s.get("xp_reward", 50)
            )
            for s in DIAGNOSTIC_SCENARIOS
        ]

    @staticmethod
    def get_scenario(scenario_id: str) -> DiagnosticScenarioDetail:
        scenario = next((s for s in DIAGNOSTIC_SCENARIOS if s["id"] == scenario_id), None)
        if not scenario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Diagnostic scenario '{scenario_id}' was not found."
            )
        return DiagnosticScenarioDetail(**scenario)

    @staticmethod
    def evaluate_diagnosis(submission: DiagnosticSubmissionRequest) -> DiagnosticSubmissionResponse:
        scenario = next((s for s in DIAGNOSTIC_SCENARIOS if s["id"] == submission.scenario_id), None)
        if not scenario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Diagnostic scenario '{submission.scenario_id}' was not found."
            )

        is_correct = (submission.selected_option == scenario["correct_option"])
        return DiagnosticSubmissionResponse(
            scenario_id=scenario["id"],
            is_correct=is_correct,
            explanation=scenario["explanation"],
            fix_code_snippet=scenario["fix_code_snippet"],
            points_earned=scenario["xp_reward"] if is_correct else 0,
            concept_mastered=scenario["concept_mastered"]
        )
