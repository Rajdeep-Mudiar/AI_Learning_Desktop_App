import time
from typing import List, Dict, Any, Optional
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.schemas.challenge import (
    ChallengeSummary, ChallengeDetail, ChallengeSubmissionRequest,
    ChallengeSubmissionResponse, TestCaseResult
)
from app.sandbox.executor import SandboxExecutor
from app.schemas.sandbox import CodeExecutionRequest
from app.repositories.user_repository import UserRepository

CHALLENGES_STORE = [
    {
        "id": "linear-regression-ols",
        "title": "Ordinary Least Squares (OLS) from Scratch",
        "category": "Linear Models",
        "difficulty": "Beginner",
        "description": "Implement the closed-form Normal Equation w = (XᵀX)⁻¹ Xᵀy in pure NumPy to compute optimal regression weights.",
        "skills_tested": ["NumPy Matrix Ops", "Linear Algebra", "OLS Formulation"],
        "xp_reward": 100,
        "problem_statement": (
            "Write a function `fit_ols(X: np.ndarray, y: np.ndarray) -> np.ndarray` that computes the closed-form "
            "weights vector w using the Normal Equation:\n\n"
            "$$\\mathbf{w} = (\\mathbf{X}^T \\mathbf{X})^{-1} \\mathbf{X}^T \\mathbf{y}$$\n\n"
            "Requirements:\n"
            "- Assume X has shape (N, D) and y has shape (N, 1) or (N,).\n"
            "- Return w as a 1D NumPy array or (D, 1) matrix.\n"
            "- Use `np.linalg.inv` or `np.linalg.pinv`."
        ),
        "starter_code": (
            "import numpy as np\n\n"
            "def fit_ols(X: np.ndarray, y: np.ndarray) -> np.ndarray:\n"
            "    # Your implementation here:\n"
            "    # w = (X^T * X)^(-1) * X^T * y\n"
            "    pass\n"
        ),
        "hints": [
            "Hint 1: Recall that matrix multiplication in NumPy is `np.matmul(A, B)` or `A @ B`.",
            "Hint 2: The transpose of matrix X is `X.T`.",
            "Hint 3: `np.linalg.inv(X.T @ X) @ X.T @ y` solves for w directly."
        ],
        "test_harness_code": (
            "\n"
            "# Autograder harness\n"
            "import json, sys\n"
            "results = []\n"
            "try:\n"
            "    # Test 1: Simple 1D line y = 2x\n"
            "    X1 = np.array([[1.0], [2.0], [3.0]])\n"
            "    y1 = np.array([2.0, 4.0, 6.0])\n"
            "    w1 = fit_ols(X1, y1)\n"
            "    passed1 = np.isclose(float(w1[0]), 2.0, atol=1e-3)\n"
            "    results.append({'test_id': 't1', 'desc': 'Simple 1D line (y=2x)', 'passed': bool(passed1), 'expected': '2.0', 'actual': str(round(float(w1[0]), 3))})\n"
            "\n"
            "    # Test 2: Multi-feature (3 variables)\n"
            "    X2 = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])\n"
            "    y2 = np.array([3.0, 5.0, 8.0])\n"
            "    w2 = fit_ols(X2, y2)\n"
            "    passed2 = np.allclose(w2.flatten(), [3.0, 5.0], atol=1e-3)\n"
            "    results.append({'test_id': 't2', 'desc': 'Multi-feature 2D parameters', 'passed': bool(passed2), 'expected': '[3.0, 5.0]', 'actual': str(np.round(w2.flatten(), 2).tolist())})\n"
            "\n"
            "    # Test 3: Hidden test with noise\n"
            "    np.random.seed(42)\n"
            "    X3 = np.random.randn(20, 3)\n"
            "    true_w = np.array([1.5, -2.0, 4.0])\n"
            "    y3 = X3 @ true_w\n"
            "    w3 = fit_ols(X3, y3)\n"
            "    passed3 = np.allclose(w3.flatten(), true_w, atol=1e-3)\n"
            "    results.append({'test_id': 't3', 'desc': 'Hidden verification batch', 'passed': bool(passed3), 'is_hidden': True})\n"
            "except Exception as e:\n"
            "    results.append({'test_id': 'err', 'desc': 'Runtime Execution', 'passed': False, 'error': str(e)})\n"
            "print('---TEST_RESULTS_START---')\n"
            "print(json.dumps(results))\n"
        )
    },
    {
        "id": "knn-classifier-scratch",
        "title": "K-Nearest Neighbors Classifier",
        "category": "Classification",
        "difficulty": "Intermediate",
        "description": "Implement the KNN prediction algorithm using Euclidean distance and majority voting from scratch.",
        "skills_tested": ["KNN", "Distance Metrics", "Broadcasting"],
        "xp_reward": 100,
        "problem_statement": (
            "Implement a function `predict_knn(X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray, k: int) -> np.ndarray`\n\n"
            "For each sample in X_test:\n"
            "1. Compute Euclidean distance to all samples in X_train.\n"
            "2. Find the k nearest neighbors.\n"
            "3. Take the majority vote (mode) of their class labels.\n"
            "4. Return an array of predicted class labels for X_test."
        ),
        "starter_code": (
            "import numpy as np\n\n"
            "def predict_knn(X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray, k: int = 3) -> np.ndarray:\n"
            "    predictions = []\n"
            "    # Your code here:\n"
            "    return np.array(predictions)\n"
        ),
        "hints": [
            "Hint 1: Compute Euclidean distance using `np.linalg.norm(x_test_i - X_train, axis=1)`.",
            "Hint 2: Use `np.argsort(distances)[:k]` to get indices of the k smallest distances.",
            "Hint 3: Use `np.bincount(y_train[nearest_indices]).argmax()` for majority voting."
        ],
        "test_harness_code": (
            "\n"
            "import json, sys\n"
            "results = []\n"
            "try:\n"
            "    X_tr = np.array([[0, 0], [1, 1], [5, 5], [6, 6]])\n"
            "    y_tr = np.array([0, 0, 1, 1])\n"
            "    X_te = np.array([[0.5, 0.5], [5.5, 5.5]])\n"
            "    preds = predict_knn(X_tr, y_tr, X_te, k=1)\n"
            "    passed1 = list(preds) == [0, 1]\n"
            "    results.append({'test_id': 't1', 'desc': '2-Cluster binary separation (k=1)', 'passed': bool(passed1), 'expected': '[0, 1]', 'actual': str(list(preds))})\n"
            "\n"
            "    preds_k3 = predict_knn(X_tr, y_tr, X_te, k=3)\n"
            "    passed2 = list(preds_k3) == [0, 1]\n"
            "    results.append({'test_id': 't2', 'desc': 'Majority voting resolution (k=3)', 'passed': bool(passed2), 'expected': '[0, 1]', 'actual': str(list(preds_k3))})\n"
            "except Exception as e:\n"
            "    results.append({'test_id': 'err', 'desc': 'Runtime', 'passed': False, 'error': str(e)})\n"
            "print('---TEST_RESULTS_START---')\n"
            "print(json.dumps(results))\n"
        )
    },
    {
        "id": "gini-impurity-scratch",
        "title": "Gini Impurity Calculator",
        "category": "Decision Trees",
        "difficulty": "Beginner",
        "description": "Calculate Gini Impurity for a set of class labels, the foundation of Decision Tree split criteria.",
        "skills_tested": ["Decision Trees", "Gini Impurity", "Probability"],
        "xp_reward": 100,
        "problem_statement": (
            "Write a function `calculate_gini(labels: np.ndarray) -> float`\n\n"
            "Formula:\n"
            "$$Gini = 1 - \\sum_{i=1}^C p_i^2$$\n"
            "where $p_i$ is the relative frequency of class $i$.\n\n"
            "- Return 0.0 for pure nodes (all samples same class).\n"
            "- Round result to 4 decimal places."
        ),
        "starter_code": (
            "import numpy as np\n\n"
            "def calculate_gini(labels: np.ndarray) -> float:\n"
            "    if len(labels) == 0:\n"
            "        return 0.0\n"
            "    # Your implementation:\n"
            "    pass\n"
        ),
        "hints": [
            "Hint 1: Count unique class occurrences using `np.unique(labels, return_counts=True)`.",
            "Hint 2: Probabilities $p_i = counts / len(labels)$.",
            "Hint 3: Subtract the sum of squared probabilities from 1.0."
        ],
        "test_harness_code": (
            "\n"
            "import json\n"
            "results = []\n"
            "try:\n"
            "    g1 = calculate_gini(np.array([0, 0, 0, 0]))\n"
            "    p1 = np.isclose(g1, 0.0, atol=1e-3)\n"
            "    results.append({'test_id': 't1', 'desc': 'Pure node test (all class 0)', 'passed': bool(p1), 'expected': '0.0', 'actual': str(g1)})\n"
            "\n"
            "    g2 = calculate_gini(np.array([0, 1]))\n"
            "    p2 = np.isclose(g2, 0.5, atol=1e-3)\n"
            "    results.append({'test_id': 't2', 'desc': '50/50 binary split', 'passed': bool(p2), 'expected': '0.5', 'actual': str(g2)})\n"
            "except Exception as e:\n"
            "    results.append({'test_id': 'err', 'desc': 'Execution error', 'passed': False, 'error': str(e)})\n"
            "print('---TEST_RESULTS_START---')\n"
            "print(json.dumps(results))\n"
        )
    }
]

class ChallengeService:
    @staticmethod
    def list_challenges() -> List[ChallengeSummary]:
        return [
            ChallengeSummary(
                id=c["id"],
                title=c["title"],
                category=c["category"],
                difficulty=c["difficulty"],
                description=c["description"],
                skills_tested=c["skills_tested"],
                xp_reward=c.get("xp_reward", 100),
                is_completed=False
            )
            for c in CHALLENGES_STORE
        ]

    @staticmethod
    def get_challenge(challenge_id: str) -> ChallengeDetail:
        challenge = next((c for c in CHALLENGES_STORE if c["id"] == challenge_id), None)
        if not challenge:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Challenge '{challenge_id}' was not found."
            )
        return ChallengeDetail(
            id=challenge["id"],
            title=challenge["title"],
            category=challenge["category"],
            difficulty=challenge["difficulty"],
            description=challenge["description"],
            skills_tested=challenge["skills_tested"],
            xp_reward=challenge.get("xp_reward", 100),
            problem_statement=challenge["problem_statement"],
            starter_code=challenge["starter_code"],
            hints=challenge["hints"],
            visible_test_cases_count=2,
            total_test_cases_count=3
        )

    @staticmethod
    async def grade_submission(submission: ChallengeSubmissionRequest, user_id: str, db: AsyncIOMotorDatabase) -> ChallengeSubmissionResponse:
        challenge = next((c for c in CHALLENGES_STORE if c["id"] == submission.challenge_id), None)
        if not challenge:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Challenge '{submission.challenge_id}' was not found."
            )

        # Build full executable test script by appending the test harness
        full_code = f"{submission.code}\n{challenge['test_harness_code']}"

        exec_res = await SandboxExecutor.execute_code(CodeExecutionRequest(
            code=full_code,
            timeout_seconds=6.0
        ))

        test_results = []
        all_passed = False

        if exec_res.status == "success" and "---TEST_RESULTS_START---" in exec_res.stdout:
            try:
                import json
                parts = exec_res.stdout.split("---TEST_RESULTS_START---")
                json_str = parts[1].strip().split("\n")[0]
                raw_results = json.loads(json_str)

                for r in raw_results:
                    test_results.append(TestCaseResult(
                        test_id=r.get("test_id", "t"),
                        description=r.get("desc", "Test case"),
                        passed=r.get("passed", False),
                        expected_output=r.get("expected"),
                        actual_output=r.get("actual"),
                        error_message=r.get("error"),
                        is_hidden=r.get("is_hidden", False)
                    ))
                all_passed = all(t.passed for t in test_results)
            except Exception as parse_err:
                test_results.append(TestCaseResult(
                    test_id="err",
                    description="Result parsing",
                    passed=False,
                    error_message=f"Output parsing error: {str(parse_err)}"
                ))
        else:
            # Syntax / Runtime / Timeout error
            err_msg = exec_res.stderr if exec_res.stderr else "Execution failed with non-zero exit code."
            test_results.append(TestCaseResult(
                test_id="exec_err",
                description="Sandbox Execution & Syntax",
                passed=False,
                error_message=err_msg
            ))

        passed_count = sum(1 for t in test_results if t.passed)
        total_count = len(test_results)

        # If all passed, reward user skill mastery and XP
        skill_updates = {}
        if all_passed:
            user_repo = UserRepository(db)
            for skill in challenge.get("skills_tested", []):
                skill_updates = await user_repo.update_skill_mastery(user_id, "supervised_learning", 10.0)

        feedback = (
            f"Spectacular! All {total_count} unit tests and hidden verification checks passed!"
            if all_passed else
            f"{passed_count} of {total_count} test cases passed. Review failing outputs and hints to debug."
        )

        return ChallengeSubmissionResponse(
            challenge_id=challenge["id"],
            all_passed=all_passed,
            passed_count=passed_count,
            total_count=total_count,
            test_results=test_results,
            execution_duration_ms=exec_res.duration_ms,
            xp_earned=challenge["xp_reward"] if all_passed else 0,
            feedback_message=feedback,
            skill_updates=skill_updates
        )
