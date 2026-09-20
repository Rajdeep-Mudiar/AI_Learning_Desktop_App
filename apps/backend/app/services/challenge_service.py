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
    },
    # ================= WEB DEV CHALLENGE =================
    {
        "id": "web-css-specificity",
        "title": "CSS Selector Specificity Engine",
        "domain": "web-dev",
        "category": "Web Development",
        "difficulty": "Beginner",
        "description": "Compute the CSS specificity tuple (IDs, Classes/Attributes, Elements) for a given CSS selector.",
        "skills_tested": ["CSS Specificity", "Selector Parsing", "DOM Modeling"],
        "xp_reward": 100,
        "problem_statement": (
            "Write a function `calculate_specificity(selector: str) -> tuple` that returns `(ids, classes, tags)` counts.\n\n"
            "Rules:\n"
            "- `#id` increments IDs.\n"
            "- `.class` or `[attr]` increments classes/attributes.\n"
            "- Standard element tags (`div`, `p`, `span`, `h1`) increment tags.\n"
            "- Return a 3-tuple `(ids, classes, tags)`."
        ),
        "starter_code": (
            "import re\n\n"
            "def calculate_specificity(selector: str) -> tuple:\n"
            "    # Return (ids, classes, tags)\n"
            "    pass\n"
        ),
        "hints": [
            "Hint 1: Count '#' occurrences for IDs.",
            "Hint 2: Count '.' occurrences for classes.",
            "Hint 3: Strip IDs and classes to isolate remaining tag names."
        ],
        "test_harness_code": (
            "\n"
            "import json\n"
            "results = []\n"
            "try:\n"
            "    r1 = calculate_specificity('#main .nav-item a')\n"
            "    p1 = r1 == (1, 1, 1)\n"
            "    results.append({'test_id': 't1', 'desc': '#main .nav-item a -> (1, 1, 1)', 'passed': bool(p1), 'expected': '(1, 1, 1)', 'actual': str(r1)})\n"
            "\n"
            "    r2 = calculate_specificity('div.card')\n"
            "    p2 = r2 == (0, 1, 1)\n"
            "    results.append({'test_id': 't2', 'desc': 'div.card -> (0, 1, 1)', 'passed': bool(p2), 'expected': '(0, 1, 1)', 'actual': str(r2)})\n"
            "except Exception as e:\n"
            "    results.append({'test_id': 'err', 'desc': 'Runtime error', 'passed': False, 'error': str(e)})\n"
            "print('---TEST_RESULTS_START---')\n"
            "print(json.dumps(results))\n"
        )
    },
    # ================= APP DEV CHALLENGE =================
    {
        "id": "app-viewport-clamp",
        "title": "Mobile Viewport Touch Target Clamp",
        "domain": "app-dev",
        "category": "App Development",
        "difficulty": "Beginner",
        "description": "Ensure interactive touch targets meet Apple Human Interface (44x44pt) and Android Material (48x48dp) minimum boundaries.",
        "skills_tested": ["Touch Targets", "Mobile Viewports", "UI Constraints"],
        "xp_reward": 100,
        "problem_statement": (
            "Write a function `clamp_touch_target(width: float, height: float, os_type: str = 'ios') -> tuple`\n\n"
            "- For 'ios': minimum size is (44.0, 44.0).\n"
            "- For 'android': minimum size is (48.0, 48.0).\n"
            "- If input dimension is smaller, expand to minimum. If larger, leave as is.\n"
            "- Return `(clamped_w, clamped_h)`."
        ),
        "starter_code": (
            "def clamp_touch_target(width: float, height: float, os_type: str = 'ios') -> tuple:\n"
            "    # Your implementation:\n"
            "    pass\n"
        ),
        "hints": [
            "Hint: Use `max(width, min_val)` for both dimensions."
        ],
        "test_harness_code": (
            "\n"
            "import json\n"
            "results = []\n"
            "try:\n"
            "    r1 = clamp_touch_target(32.0, 20.0, 'ios')\n"
            "    p1 = r1 == (44.0, 44.0)\n"
            "    results.append({'test_id': 't1', 'desc': 'iOS touch target expansion to 44pt', 'passed': bool(p1), 'expected': '(44.0, 44.0)', 'actual': str(r1)})\n"
            "\n"
            "    r2 = clamp_touch_target(60.0, 30.0, 'android')\n"
            "    p2 = r2 == (60.0, 48.0)\n"
            "    results.append({'test_id': 't2', 'desc': 'Android touch height expansion to 48dp', 'passed': bool(p2), 'expected': '(60.0, 48.0)', 'actual': str(r2)})\n"
            "except Exception as e:\n"
            "    results.append({'test_id': 'err', 'desc': 'Runtime error', 'passed': False, 'error': str(e)})\n"
            "print('---TEST_RESULTS_START---')\n"
            "print(json.dumps(results))\n"
        )
    },
    # ================= SYSTEM DESIGN CHALLENGE =================
    {
        "id": "sys-token-bucket",
        "title": "Token Bucket Rate Limiter",
        "domain": "system-design",
        "category": "System Design",
        "difficulty": "Intermediate",
        "description": "Implement a deterministic token bucket rate limiter to prevent server DDoS and API starvation.",
        "skills_tested": ["Rate Limiting", "Token Bucket", "Traffic Shaping"],
        "xp_reward": 150,
        "problem_statement": (
            "Write a class `TokenBucket(capacity: int, refill_rate_per_sec: float)` with method:\n"
            "`allow_request(tokens_requested: int, current_time_sec: float) -> bool`\n\n"
            "- Refill tokens proportionally based on elapsed time since last request up to `capacity`.\n"
            "- If available tokens >= tokens_requested, deduct tokens and return True, else return False."
        ),
        "starter_code": (
            "class TokenBucket:\n"
            "    def __init__(self, capacity: int, refill_rate_per_sec: float):\n"
            "        self.capacity = float(capacity)\n"
            "        self.refill_rate = float(refill_rate_per_sec)\n"
            "        self.tokens = float(capacity)\n"
            "        self.last_time = 0.0\n\n"
            "    def allow_request(self, tokens_requested: int, current_time_sec: float) -> bool:\n"
            "        pass\n"
        ),
        "hints": [
            "Hint: elapsed = current_time_sec - self.last_time; self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)."
        ],
        "test_harness_code": (
            "\n"
            "import json\n"
            "results = []\n"
            "try:\n"
            "    tb = TokenBucket(capacity=5, refill_rate_per_sec=1.0)\n"
            "    tb.last_time = 0.0\n"
            "    r1 = tb.allow_request(3, 0.0)  # tokens left: 2\n"
            "    r2 = tb.allow_request(3, 0.0)  # rejected (only 2 left)\n"
            "    r3 = tb.allow_request(2, 2.0)  # refilled +2 -> 4 tokens -> allows 2\n"
            "    p = (r1 is True) and (r2 is False) and (r3 is True)\n"
            "    results.append({'test_id': 't1', 'desc': 'Capacity drain and refill sequence', 'passed': bool(p), 'expected': 'True, False, True', 'actual': f'{r1}, {r2}, {r3}'})\n"
            "except Exception as e:\n"
            "    results.append({'test_id': 'err', 'desc': 'Execution error', 'passed': False, 'error': str(e)})\n"
            "print('---TEST_RESULTS_START---')\n"
            "print(json.dumps(results))\n"
        )
    },
    # ================= GIT & GITHUB CHALLENGES =================
    {
        "id": "git-fast-forward",
        "title": "Git Fast-Forward Merge Validator",
        "domain": "github",
        "category": "Git & GitHub",
        "difficulty": "Beginner",
        "description": "Determine whether branch B can be fast-forward merged into branch A given a commit parent map.",
        "skills_tested": ["Git Commit Graph", "DAG Traversal", "Branch Pointers"],
        "xp_reward": 100,
        "problem_statement": (
            "Write a function `can_fast_forward(parent_map: dict, target_branch_commit: str, source_branch_commit: str) -> bool`\n\n"
            "`parent_map` maps `commit_id -> list_of_parent_commit_ids`.\n"
            "A fast-forward merge from source into target is possible if `target_branch_commit` is a direct ancestor of `source_branch_commit`."
        ),
        "starter_code": (
            "def can_fast_forward(parent_map: dict, target_branch_commit: str, source_branch_commit: str) -> bool:\n"
            "    # Return True if target is an ancestor of source\n"
            "    pass\n"
        ),
        "hints": [
            "Hint: Traverse upwards from source_branch_commit using BFS or DFS."
        ],
        "test_harness_code": (
            "\n"
            "import json\n"
            "results = []\n"
            "try:\n"
            "    dag = {'C1': [], 'C2': ['C1'], 'C3': ['C2'], 'C4': ['C1']}\n"
            "    r1 = can_fast_forward(dag, 'C1', 'C3')  # C1 is ancestor of C3 -> True\n"
            "    r2 = can_fast_forward(dag, 'C4', 'C3')  # C4 is on different branch -> False\n"
            "    p = (r1 is True) and (r2 is False)\n"
            "    results.append({'test_id': 't1', 'desc': 'Direct ancestor line detection', 'passed': bool(p), 'expected': 'True, False', 'actual': f'{r1}, {r2}'})\n"
            "except Exception as e:\n"
            "    results.append({'test_id': 'err', 'desc': 'Execution error', 'passed': False, 'error': str(e)})\n"
            "print('---TEST_RESULTS_START---')\n"
            "print(json.dumps(results))\n"
        )
    },
    {
        "id": "git-merge-base",
        "title": "Git 3-Way Merge Base Finder (LCA)",
        "domain": "github",
        "category": "Git & GitHub",
        "difficulty": "Intermediate",
        "description": "Find the lowest common ancestor (merge-base) commit between two branch tips in a Git commit DAG.",
        "skills_tested": ["Git 3-Way Merge", "Lowest Common Ancestor", "DAG Graph"],
        "xp_reward": 150,
        "problem_statement": (
            "Write a function `find_merge_base(parent_map: dict, commit_a: str, commit_b: str) -> str`\n\n"
            "Given a directed acyclic graph `parent_map` mapping each commit to a list of parent commit IDs,\n"
            "find the most recent common ancestor commit between `commit_a` and `commit_b` (equivalent to `git merge-base`)."
        ),
        "starter_code": (
            "def find_merge_base(parent_map: dict, commit_a: str, commit_b: str) -> str:\n"
            "    # Return the commit_id of the most recent common ancestor\n"
            "    pass\n"
        ),
        "hints": [
            "Hint: Collect all ancestors of commit_a into a set, then perform a BFS from commit_b to find the first common node."
        ],
        "test_harness_code": (
            "\n"
            "import json\n"
            "results = []\n"
            "try:\n"
            "    dag = {'c1': [], 'c2': ['c1'], 'c3': ['c2'], 'c4': ['c2'], 'c5': ['c3'], 'c6': ['c4']}\n"
            "    res = find_merge_base(dag, 'c5', 'c6')\n"
            "    p = res == 'c2'\n"
            "    results.append({'test_id': 't1', 'desc': 'Find lowest common ancestor c2 for c5 and c6', 'passed': bool(p), 'expected': 'c2', 'actual': str(res)})\n"
            "except Exception as e:\n"
            "    results.append({'test_id': 'err', 'desc': 'Execution error', 'passed': False, 'error': str(e)})\n"
            "print('---TEST_RESULTS_START---')\n"
            "print(json.dumps(results))\n"
        )
    },
    {
        "id": "github-pr-conflict-detector",
        "title": "GitHub PR Merge Conflict Detector",
        "domain": "github",
        "category": "Git & GitHub",
        "difficulty": "Beginner",
        "description": "Analyze file change dictionaries from two branches to detect file-level and line-range merge conflicts.",
        "skills_tested": ["Merge Conflicts", "Code Review", "Diff Processing"],
        "xp_reward": 120,
        "problem_statement": (
            "Write a function `detect_conflicts(base_branch_diffs: dict, pr_branch_diffs: dict) -> list`\n\n"
            "`base_branch_diffs` and `pr_branch_diffs` map `filename -> list_of_modified_line_numbers`.\n"
            "Return a sorted list of filenames that have overlapping line number modifications."
        ),
        "starter_code": (
            "def detect_conflicts(base_branch_diffs: dict, pr_branch_diffs: dict) -> list:\n"
            "    # Return list of conflicting filenames\n"
            "    pass\n"
        ),
        "hints": [
            "Hint: Find intersection of files, then check if set(linesA) & set(linesB) is non-empty."
        ],
        "test_harness_code": (
            "\n"
            "import json\n"
            "results = []\n"
            "try:\n"
            "    base = {'auth.py': [10, 11, 12], 'db.py': [5, 6]}\n"
            "    pr = {'auth.py': [12, 13, 14], 'db.py': [20, 21], 'routes.py': [1]}\n"
            "    res = detect_conflicts(base, pr)\n"
            "    p = res == ['auth.py']\n"
            "    results.append({'test_id': 't1', 'desc': 'Identify auth.py overlap on line 12', 'passed': bool(p), 'expected': \"['auth.py']\", 'actual': str(res)})\n"
            "except Exception as e:\n"
            "    results.append({'test_id': 'err', 'desc': 'Execution error', 'passed': False, 'error': str(e)})\n"
            "print('---TEST_RESULTS_START---')\n"
            "print(json.dumps(results))\n"
        )
    },
    {
        "id": "github-actions-matrix",
        "title": "GitHub Actions Matrix Strategy Generator",
        "domain": "github",
        "category": "Git & GitHub",
        "difficulty": "Intermediate",
        "description": "Compute all job dimension permutations for a GitHub Actions CI matrix strategy config.",
        "skills_tested": ["GitHub Actions", "Matrix Builds", "CI/CD Pipeline"],
        "xp_reward": 140,
        "problem_statement": (
            "Write a function `generate_matrix_jobs(matrix_config: dict) -> list`\n\n"
            "Given `matrix_config = {'os': ['ubuntu-latest', 'windows-latest'], 'python-version': ['3.11', '3.12']}`,\n"
            "return a list of all combination dictionaries: `[{'os': ..., 'python-version': ...}, ...]`."
        ),
        "starter_code": (
            "import itertools\n\n"
            "def generate_matrix_jobs(matrix_config: dict) -> list:\n"
            "    # Return list of all cartesian product job configs\n"
            "    pass\n"
        ),
        "hints": [
            "Hint: Use itertools.product on the dictionary values and pair with keys."
        ],
        "test_harness_code": (
            "\n"
            "import json\n"
            "results = []\n"
            "try:\n"
            "    cfg = {'os': ['ubuntu', 'windows'], 'node': ['18', '20']}\n"
            "    res = generate_matrix_jobs(cfg)\n"
            "    p = len(res) == 4 and {'os': 'ubuntu', 'node': '18'} in res\n"
            "    results.append({'test_id': 't1', 'desc': 'Generates 4 job combinations correctly', 'passed': bool(p), 'expected': '4 jobs', 'actual': f'{len(res)} jobs'})\n"
            "except Exception as e:\n"
            "    results.append({'test_id': 'err', 'desc': 'Execution error', 'passed': False, 'error': str(e)})\n"
            "print('---TEST_RESULTS_START---')\n"
            "print(json.dumps(results))\n"
        )
    },
    {
        "id": "git-blob-hasher",
        "title": "Git Object Store & SHA-1 Hasher",
        "domain": "github",
        "category": "Git & GitHub",
        "difficulty": "Beginner",
        "description": "Implement standard Git blob format serialization and compute its SHA-1 hash object ID.",
        "skills_tested": ["Git Internals", "Blob Storage", "SHA-1 Hash"],
        "xp_reward": 110,
        "problem_statement": (
            "Write a function `compute_git_blob_sha(content_str: str) -> str`\n\n"
            "In Git, a blob is formatted as: `blob <byte_length>\\0<content_bytes>`.\n"
            "Compute and return the hex SHA-1 digest string of this header + content."
        ),
        "starter_code": (
            "import hashlib\n\n"
            "def compute_git_blob_sha(content_str: str) -> str:\n"
            "    # Format as 'blob <len>\\0<content>' and return hashlib.sha1 hex digest\n"
            "    pass\n"
        ),
        "hints": [
            "Hint: Use b'blob ' + str(len(content_bytes)).encode() + b'\\0' + content_bytes."
        ],
        "test_harness_code": (
            "\n"
            "import json\n"
            "results = []\n"
            "try:\n"
            "    # 'hello world\\n' in git has known sha 3b18e512dba79e4c8300dd08aeb37f8e728b8dad\n"
            "    res = compute_git_blob_sha('hello world\\n')\n"
            "    p = res.lower() == '3b18e512dba79e4c8300dd08aeb37f8e728b8dad'\n"
            "    results.append({'test_id': 't1', 'desc': 'Computes exact Git blob sha for hello world', 'passed': bool(p), 'expected': '3b18e512dba79e4c8300dd08aeb37f8e728b8dad', 'actual': str(res)})\n"
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
                domain=c.get("domain", "ai-ml"),
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
            domain=challenge.get("domain", "ai-ml"),
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
