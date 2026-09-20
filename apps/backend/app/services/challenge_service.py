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
    # ================= GIT & GITHUB SITUATIONAL CHALLENGES =================
    {
        "id": "git-fast-forward",
        "title": "Git Branching & Fast-Forward Merging",
        "domain": "github",
        "category": "Git & GitHub",
        "difficulty": "Beginner",
        "challenge_type": "git-terminal",
        "description": "Situational Challenge: Create a feature branch, commit staged changes, and execute a clean fast-forward merge into main.",
        "skills_tested": ["git branch", "git checkout -b", "git add", "git commit", "git merge"],
        "xp_reward": 100,
        "problem_statement": (
            "### Scenario Background\n"
            "You are working on an authentication feature for an enterprise repository. Your task is to branch off `main`, stage & commit your security updates, and fast-forward merge your feature back into `main` without creating merge clutter.\n\n"
            "### Objectives:\n"
            "1. **Step 1:** Create and switch to a new branch called `feature/auth`.\n"
            "2. **Step 2:** Stage all modified changes and commit with message `feat: add jwt auth`.\n"
            "3. **Step 3:** Switch back to `main` and fast-forward merge `feature/auth` into `main`."
        ),
        "starter_code": "# Type Git commands in the interactive terminal on the right to complete each scenario step.",
        "hints": [
            "Step 1: Use `git checkout -b feature/auth` or `git switch -c feature/auth`.",
            "Step 2: Use `git add .` (or `git add src/auth/jwt.py`) followed by `git commit -m \"feat: add jwt auth\"`.",
            "Step 3: Use `git checkout main` and then `git merge feature/auth`."
        ],
        "scenarios": [
            {
                "step": 1,
                "title": "Create & Checkout Feature Branch",
                "instruction": "Create and switch to a new branch named `feature/auth`.",
                "hint": "Try `git checkout -b feature/auth` or `git switch -c feature/auth`",
                "accepted_patterns": ["checkout -b feature/auth", "switch -c feature/auth", "branch feature/auth"],
                "success_message": "Branch 'feature/auth' created and checked out successfully!"
            },
            {
                "step": 2,
                "title": "Stage & Commit Authentication Changes",
                "instruction": "Stage modified files and commit with message `feat: add jwt auth`.",
                "hint": "Try `git add .` then `git commit -m \"feat: add jwt auth\"`",
                "accepted_patterns": ["commit -m \"feat: add jwt auth\"", "commit -m 'feat: add jwt auth'", "commit -am \"feat: add jwt auth\""],
                "success_message": "Changes committed with message 'feat: add jwt auth' on branch feature/auth!"
            },
            {
                "step": 3,
                "title": "Fast-Forward Merge into Main",
                "instruction": "Switch back to `main` branch and fast-forward merge `feature/auth`.",
                "hint": "Try `git checkout main` followed by `git merge feature/auth`",
                "accepted_patterns": ["merge feature/auth"],
                "success_message": "Fast-forward merge completed cleanly! Branch 'main' updated to match feature/auth."
            }
        ],
        "test_harness_code": ""
    },
    {
        "id": "git-merge-base",
        "title": "Git 3-Way Merge & Conflict Resolution",
        "domain": "github",
        "category": "Git & GitHub",
        "difficulty": "Intermediate",
        "challenge_type": "git-terminal",
        "description": "Situational Challenge: Inspect divergent branch commit history, verify merge bases, and execute a 3-way merge.",
        "skills_tested": ["git log", "git merge", "3-way merge", "git status"],
        "xp_reward": 150,
        "problem_statement": (
            "### Scenario Background\n"
            "A teammate branched off to develop `feature/payments` while commits were added to `main`. You need to inspect the commit history DAG and execute a 3-way merge.\n\n"
            "### Objectives:\n"
            "1. **Step 1:** Inspect the commit DAG log history using `git log`.\n"
            "2. **Step 2:** Merge branch `feature/payments` into your current branch.\n"
            "3. **Step 3:** Check the repository status with `git status` to verify clean working tree."
        ),
        "starter_code": "# Type Git commands in the interactive terminal on the right to complete each scenario step.",
        "hints": [
            "Step 1: Run `git log` or `git log --oneline`.",
            "Step 2: Run `git merge feature/payments`.",
            "Step 3: Run `git status`."
        ],
        "scenarios": [
            {
                "step": 1,
                "title": "Inspect Commit DAG Graph",
                "instruction": "Inspect the linear commit DAG history.",
                "hint": "Run `git log`",
                "accepted_patterns": ["git log", "log"],
                "success_message": "DAG commit history displayed from HEAD to root commit."
            },
            {
                "step": 2,
                "title": "Execute 3-Way Merge",
                "instruction": "Merge branch `feature/payments` into `main`.",
                "hint": "Run `git merge feature/payments`",
                "accepted_patterns": ["merge feature/payments"],
                "success_message": "3-way merge commit created connecting feature/payments into main!"
            },
            {
                "step": 3,
                "title": "Verify Repository Status",
                "instruction": "Verify working tree and staging index status.",
                "hint": "Run `git status`",
                "accepted_patterns": ["git status", "status"],
                "success_message": "Repository status verified clean after merge!"
            }
        ],
        "test_harness_code": ""
    },
    {
        "id": "github-pr-conflict-detector",
        "title": "GitHub Pull Request & Code Review Workflow",
        "domain": "github",
        "category": "Git & GitHub",
        "difficulty": "Beginner",
        "challenge_type": "git-terminal",
        "description": "Situational Challenge: List open Pull Requests via GitHub CLI (gh), checkout PR code, and merge into production.",
        "skills_tested": ["gh pr list", "gh pr checkout", "gh pr view", "gh pr merge"],
        "xp_reward": 120,
        "problem_statement": (
            "### Scenario Background\n"
            "You are reviewing open pull requests on the remote GitHub repository. You need to use the GitHub CLI (`gh`) to list open PRs, inspect PR #42, and merge it.\n\n"
            "### Objectives:\n"
            "1. **Step 1:** List all open pull requests with `gh pr list`.\n"
            "2. **Step 2:** Checkout Pull Request #42 using `gh pr checkout 42`.\n"
            "3. **Step 3:** Merge Pull Request #42 with `gh pr merge 42`."
        ),
        "starter_code": "# Type GitHub CLI (gh) commands in the interactive terminal on the right.",
        "hints": [
            "Step 1: Run `gh pr list`.",
            "Step 2: Run `gh pr checkout 42`.",
            "Step 3: Run `gh pr merge 42` or `gh pr merge`."
        ],
        "scenarios": [
            {
                "step": 1,
                "title": "List Open Pull Requests",
                "instruction": "List all active pull requests in the repository using `gh pr list`.",
                "hint": "Type `gh pr list`",
                "accepted_patterns": ["gh pr list", "pr list"],
                "success_message": "Found 3 open Pull Requests: #42 (JWT Auth), #43 (DB Pool), #44 (CI Matrix)."
            },
            {
                "step": 2,
                "title": "Checkout Pull Request #42",
                "instruction": "Checkout Pull Request #42 to inspect its local branch.",
                "hint": "Type `gh pr checkout 42`",
                "accepted_patterns": ["gh pr checkout 42", "gh pr checkout #42", "checkout feature/auth"],
                "success_message": "Switched to branch 'feature/auth' from Pull Request #42."
            },
            {
                "step": 3,
                "title": "Merge Pull Request #42",
                "instruction": "Merge Pull Request #42 into main.",
                "hint": "Type `gh pr merge 42` or `gh pr merge`",
                "accepted_patterns": ["gh pr merge", "pr merge"],
                "success_message": "Pull Request #42 approved and merged into main successfully!"
            }
        ],
        "test_harness_code": ""
    },
    {
        "id": "github-actions-matrix",
        "title": "GitHub Actions CI/CD Matrix & Automated Pipeline",
        "domain": "github",
        "category": "Git & GitHub",
        "difficulty": "Intermediate",
        "challenge_type": "git-terminal",
        "description": "Situational Challenge: Inspect GitHub Actions CI/CD workflows, trigger pipeline execution, and create release tags.",
        "skills_tested": ["gh workflow list", "gh workflow run", "git tag", "Release Pointers"],
        "xp_reward": 140,
        "problem_statement": (
            "### Scenario Background\n"
            "Your team is deploying a new version. You need to inspect active GitHub Actions workflows, trigger a workflow dispatch build, and tag the release `v1.0.0`.\n\n"
            "### Objectives:\n"
            "1. **Step 1:** List active workflows using `gh workflow list`.\n"
            "2. **Step 2:** Trigger the automated CI/CD matrix build using `gh workflow run`.\n"
            "3. **Step 3:** Create release tag `v1.0.0` pinned to current HEAD."
        ),
        "starter_code": "# Type GitHub CLI and Git tag commands in the terminal.",
        "hints": [
            "Step 1: Run `gh workflow list`.",
            "Step 2: Run `gh workflow run`.",
            "Step 3: Run `git tag v1.0.0` or `git tag -a v1.0.0 -m \"Release v1.0.0\"`."
        ],
        "scenarios": [
            {
                "step": 1,
                "title": "List CI/CD Workflows",
                "instruction": "Inspect active workflows in `.github/workflows/` using `gh workflow list`.",
                "hint": "Type `gh workflow list`",
                "accepted_patterns": ["gh workflow list", "workflow list"],
                "success_message": "Active workflow found: 'Enterprise CI/CD Automated Deployment Matrix'."
            },
            {
                "step": 2,
                "title": "Trigger Automated Pipeline",
                "instruction": "Trigger the automated matrix test & build pipeline using `gh workflow run`.",
                "hint": "Type `gh workflow run`",
                "accepted_patterns": ["gh workflow run", "workflow run"],
                "success_message": "GitHub Actions CI/CD pipeline triggered and running test matrix!"
            },
            {
                "step": 3,
                "title": "Publish Release Tag",
                "instruction": "Tag the current commit with release version `v1.0.0`.",
                "hint": "Type `git tag v1.0.0`",
                "accepted_patterns": ["git tag v1.0.0", "tag v1.0.0", "tag -a v1.0.0"],
                "success_message": "Created release tag 'v1.0.0' pinned to current HEAD!"
            }
        ],
        "test_harness_code": ""
    },
    {
        "id": "git-blob-hasher",
        "title": "Git Staging & Safe History Rollback",
        "domain": "github",
        "category": "Git & GitHub",
        "difficulty": "Beginner",
        "challenge_type": "git-terminal",
        "description": "Situational Challenge: Unstage unwanted files, stash active modifications, and revert a faulty commit safely.",
        "skills_tested": ["git restore --staged", "git stash", "git revert", "Safe Rollback"],
        "xp_reward": 110,
        "problem_statement": (
            "### Scenario Background\n"
            "You accidentally staged a secret configuration file and discovered a bug in commit `9a01f8`. You must unstage the config file, stash your work, and revert `9a01f8`.\n\n"
            "### Objectives:\n"
            "1. **Step 1:** Unstage `config/database.env` without losing working changes.\n"
            "2. **Step 2:** Save your uncommitted modifications to the stash with `git stash`.\n"
            "3. **Step 3:** Safely revert commit `9a01f8` using `git revert 9a01f8`."
        ),
        "starter_code": "# Type Git undo and rollback commands in the terminal.",
        "hints": [
            "Step 1: Run `git restore --staged config/database.env` or `git reset config/database.env`.",
            "Step 2: Run `git stash`.",
            "Step 3: Run `git revert 9a01f8`."
        ],
        "scenarios": [
            {
                "step": 1,
                "title": "Unstage Sensitive Configuration",
                "instruction": "Unstage `config/database.env` while keeping working directory changes.",
                "hint": "Type `git restore --staged config/database.env` or `git reset config/database.env`",
                "accepted_patterns": ["restore --staged", "reset config/database.env", "reset -- config/database.env", "git reset"],
                "success_message": "Unstaged 'config/database.env' back to working directory!"
            },
            {
                "step": 2,
                "title": "Save Work to Stash",
                "instruction": "Save uncommitted modifications into the LIFO stash stack.",
                "hint": "Type `git stash`",
                "accepted_patterns": ["git stash", "stash push", "stash"],
                "success_message": "Saved uncommitted changes into stash@{0}!"
            },
            {
                "step": 3,
                "title": "Revert Faulty Commit",
                "instruction": "Safely revert commit `9a01f8` with an inverse patch commit.",
                "hint": "Type `git revert 9a01f8`",
                "accepted_patterns": ["git revert 9a01f8", "revert 9a01f8"],
                "success_message": "Created inverse forward revert commit for '9a01f8'!"
            }
        ],
        "test_harness_code": ""
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
                challenge_type=c.get("challenge_type", "python"),
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
            challenge_type=challenge.get("challenge_type", "python"),
            category=challenge["category"],
            difficulty=challenge["difficulty"],
            description=challenge["description"],
            skills_tested=challenge["skills_tested"],
            xp_reward=challenge.get("xp_reward", 100),
            problem_statement=challenge["problem_statement"],
            starter_code=challenge.get("starter_code", ""),
            hints=challenge.get("hints", []),
            scenarios=challenge.get("scenarios", None),
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
