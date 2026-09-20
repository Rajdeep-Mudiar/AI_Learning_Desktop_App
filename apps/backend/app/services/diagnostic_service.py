from typing import List, Optional
from fastapi import HTTPException, status
from app.schemas.diagnostic import (
    DiagnosticScenarioSummary, DiagnosticScenarioDetail,
    DiagnosticSubmissionRequest, DiagnosticSubmissionResponse
)

DIAGNOSTIC_SCENARIOS = [
    {
        "id": "scenario-data-leakage",
        "title": "The Suspicious 99.8% Medical Accuracy",
        "category": "Data Leakage",
        "difficulty": "Intermediate",
        "description": "An engineer built a medical diabetes classifier. The test accuracy is 99.8% in the Jupyter notebook, but upon deploying to live hospital patients, accuracy drops to random chance (52%). Inspect the full data pipeline to isolate the bug.",
        "symptoms": [
            "Notebook validation score is 99.8% (almost perfect)",
            "Production score drops to random chance (52.1%)",
            "Target feature: 'has_diabetes'"
        ],
        "code_snippet": (
            "# ========================================================\n"
            "# pipeline_inspect.py - Medical Diagnosis Pipeline\n"
            "# ========================================================\n"
            "import numpy as np\n"
            "import pandas as pd\n"
            "from sklearn.preprocessing import StandardScaler\n"
            "from sklearn.model_selection import train_test_split\n"
            "from sklearn.linear_model import LogisticRegression\n"
            "from sklearn.metrics import accuracy_score, classification_report\n\n"
            "# Step 1: Load complete patient records\n"
            "np.random.seed(42)\n"
            "n_samples = 1000\n"
            "features = np.random.randn(n_samples, 10)\n"
            "labels = (features[:, 0] * 1.5 + features[:, 1] * 0.8 + np.random.randn(n_samples) * 0.5 > 0).astype(int)\n\n"
            "df = pd.DataFrame(features, columns=[f'feature_{i}' for i in range(10)])\n"
            "df['has_diabetes'] = labels\n\n"
            "X = df.drop(columns=['has_diabetes'])\n"
            "y = df['has_diabetes']\n\n"
            "# Step 2: Normalize the data\n"
            "scaler = StandardScaler()\n"
            "# BUG HERE: fit_transform calculates mean & std across ALL rows before splitting!\n"
            "X_scaled = scaler.fit_transform(X)\n\n"
            "# Step 3: Split into train and holdout test set\n"
            "X_train, X_test, y_train, y_test = train_test_split(\n"
            "    X_scaled, y, test_size=0.2, random_state=42\n"
            ")\n\n"
            "# Step 4: Fit classification model\n"
            "model = LogisticRegression(C=1.0, max_iter=200)\n"
            "model.fit(X_train, y_train)\n\n"
            "# Step 5: Evaluate model\n"
            "train_acc = accuracy_score(y_train, model.predict(X_train))\n"
            "test_acc = accuracy_score(y_test, model.predict(X_test))\n"
            "print(f'Training Accuracy:   {train_acc:.4f}')\n"
            "print(f'Validation Accuracy: {test_acc:.4f}')\n"
        ),
        "metrics_log": {
            "Train Accuracy": "0.999",
            "Test Accuracy": "0.998",
            "Production Accuracy": "0.521",
            "Samples": "1,000",
            "Features": "10"
        },
        "hints": [
            "Check when the StandardScaler computes its mean and variance.",
            "Does the scaler have access to statistics from the test split before the split occurs?",
            "Preprocessing transformers must ONLY be fit on the training partition!"
        ],
        "options": [
            "The Logistic Regression regularizer C parameter is too large",
            "Preprocessing Data Leakage: StandardScaler.fit_transform was executed on the full dataset before train/test splitting",
            "The test_size parameter of 0.2 is too small",
            "LogisticRegression cannot handle standardized features"
        ],
        "correct_option": 1,
        "explanation": "Data Leakage occurs when information outside the training dataset is used during preprocessing. Calling `scaler.fit_transform(X)` on the whole dataset leaks test set statistics into the training pipeline. In production with unseen distributions, performance collapses.",
        "fix_code_snippet": (
            "# Correct Pipeline:\n"
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n"
            "scaler = StandardScaler()\n"
            "X_train_scaled = scaler.fit_transform(X_train)  # Fit ONLY on training data\n"
            "X_test_scaled = scaler.transform(X_test)        # Transform test data using train stats"
        ),
        "concept_mastered": "Data Leakage & Preprocessing Partitioning",
        "xp_reward": 50
    },
    {
        "id": "scenario-overfitting-polynomial",
        "title": "The Wild Rollercoaster Fit (High Variance)",
        "category": "Overfitting & Complexity",
        "difficulty": "Beginner",
        "description": "With a small dataset of 15 samples, the model achieves 0.000 training error, but when given new test points, the predictions oscillate wildly and yield massive errors.",
        "symptoms": [
            "Training MSE: 0.000 (Perfect training fit)",
            "Test MSE: 4892.45 (Catastrophic error)",
            "Coefficients explode up to 10^7"
        ],
        "code_snippet": (
            "# ========================================================\n"
            "# pipeline_inspect.py - Polynomial Regression Fit\n"
            "# ========================================================\n"
            "import numpy as np\n"
            "from sklearn.preprocessing import PolynomialFeatures\n"
            "from sklearn.linear_model import LinearRegression\n"
            "from sklearn.metrics import mean_squared_error\n\n"
            "# 15 small training data points\n"
            "np.random.seed(42)\n"
            "X_train = np.linspace(-3, 3, 15).reshape(-1, 1)\n"
            "y_train = np.sin(X_train).ravel() + np.random.randn(15) * 0.1\n\n"
            "X_test = np.linspace(-3, 3, 50).reshape(-1, 1)\n"
            "y_test = np.sin(X_test).ravel() + np.random.randn(50) * 0.1\n\n"
            "# Polynomial expansion of degree 14 on 15 points!\n"
            "poly = PolynomialFeatures(degree=14, include_bias=False)\n"
            "X_train_poly = poly.fit_transform(X_train)\n"
            "X_test_poly = poly.transform(X_test)\n\n"
            "model = LinearRegression()\n"
            "model.fit(X_train_poly, y_train)\n\n"
            "train_mse = mean_squared_error(y_train, model.predict(X_train_poly))\n"
            "test_mse = mean_squared_error(y_test, model.predict(X_test_poly))\n"
            "print(f'Train MSE: {train_mse:.4f}')\n"
            "print(f'Test MSE:  {test_mse:.4f}')\n"
        ),
        "metrics_log": {
            "Training Samples": 15,
            "Polynomial Degree": 14,
            "Parameters (Weights)": 14,
            "Train Loss (MSE)": "0.000",
            "Test Loss (MSE)": "4892.45"
        },
        "hints": [
            "A degree-14 polynomial has 14 weight parameters for only 15 points.",
            "When parameter count approaches sample size, the model memorizes noise (High Variance)."
        ],
        "options": [
            "The model is suffering from High Bias (Underfitting)",
            "Extreme Overfitting (High Variance): Degree 14 polynomial on 15 samples memorizes data noise",
            "LinearRegression cannot handle floating point numbers",
            "The sine function cannot be modeled with regression"
        ],
        "correct_option": 1,
        "explanation": "When polynomial degree is high relative to sample count, the curve contorts through every single point, creating wild oscillations between data points. Fix by reducing degree or adding L2 regularization (Ridge).",
        "fix_code_snippet": (
            "# Fix with moderate degree and L2 Regularization:\n"
            "from sklearn.linear_model import Ridge\n"
            "poly = PolynomialFeatures(degree=3, include_bias=False)\n"
            "model = Ridge(alpha=1.0)\n"
            "model.fit(poly.fit_transform(X_train), y_train)"
        ),
        "concept_mastered": "Bias-Variance Tradeoff & Model Capacity",
        "xp_reward": 50
    },
    {
        "id": "scenario-class-imbalance",
        "title": "The Fraud Detection Illusion",
        "category": "Class Imbalance",
        "difficulty": "Beginner",
        "description": "A fraud detection model reports 99.2% accuracy. However, in production, zero fraudulent transactions are caught. Find why accuracy is misleading.",
        "symptoms": [
            "Reported Accuracy: 99.2%",
            "Recall on Fraud Class: 0.000",
            "Confusion Matrix shows zero true positive fraud predictions"
        ],
        "code_snippet": (
            "# ========================================================\n"
            "# pipeline_inspect.py - Credit Card Fraud Classifier\n"
            "# ========================================================\n"
            "import numpy as np\n"
            "from sklearn.linear_model import LogisticRegression\n"
            "from sklearn.metrics import accuracy_score, confusion_matrix, classification_report\n\n"
            "# Imbalanced dataset: 992 legitimate transactions (0), 8 fraud (1)\n"
            "np.random.seed(42)\n"
            "X_train = np.random.randn(1000, 5)\n"
            "y_train = np.zeros(1000, dtype=int)\n"
            "y_train[:8] = 1  # only 0.8% fraud\n\n"
            "X_test = np.random.randn(500, 5)\n"
            "y_test = np.zeros(500, dtype=int)\n"
            "y_test[:4] = 1\n\n"
            "model = LogisticRegression()\n"
            "model.fit(X_train, y_train)\n\n"
            "y_pred = model.predict(X_test)\n"
            "print('Accuracy Score:', accuracy_score(y_test, y_pred))\n"
            "print('Confusion Matrix:\\n', confusion_matrix(y_test, y_pred))\n"
        ),
        "metrics_log": {
            "Total Test Samples": 500,
            "Legitimate Transactions": 496,
            "Fraudulent Transactions": 4,
            "Model Predicted Fraud": 0,
            "Accuracy": "99.2%"
        },
        "hints": [
            "If a model simply predicts 'Legitimate' for every transaction, what would its accuracy be?",
            "Look at Precision, Recall, and F1-Score instead of raw Accuracy."
        ],
        "options": [
            "Accuracy is misleading due to severe Class Imbalance; the model learned a trivial majority-class classifier",
            "The dataset has missing NaN values",
            "The model learning rate is too small",
            "Logistic Regression cannot perform binary classification"
        ],
        "correct_option": 0,
        "explanation": "On an imbalanced dataset (99.2% negative, 0.8% positive), a dummy classifier predicting class 0 always achieves 99.2% accuracy while finding zero fraud cases. Use Precision-Recall AUC, F1-Score, and class weighting (`class_weight='balanced'`).",
        "fix_code_snippet": (
            "# Use balanced class weighting and evaluate F1/Recall:\n"
            "model = LogisticRegression(class_weight='balanced')\n"
            "model.fit(X_train, y_train)\n"
            "print(classification_report(y_test, model.predict(X_test)))"
        ),
        "concept_mastered": "Class Imbalance & Metric Selection (F1 / Recall vs Accuracy)",
        "xp_reward": 50
    },
    {
        "id": "scenario-feature-scaling-distance",
        "title": "The Dominant Feature Problem in KNN",
        "category": "Data Quality",
        "difficulty": "Beginner",
        "description": "A KNN model predicts customer churn based on Age (18–80) and Annual Income ($20,000–$250,000). The model completely ignores Age and produces inaccurate predictions.",
        "symptoms": [
            "Feature 1: Age (Range: 18 - 80)",
            "Feature 2: Annual Income (Range: $20,000 - $250,000)",
            "KNN distance calculations are 99.99% driven by Income alone"
        ],
        "code_snippet": (
            "# ========================================================\n"
            "# pipeline_inspect.py - KNN Customer Churn Predictor\n"
            "# ========================================================\n"
            "import numpy as np\n"
            "from sklearn.neighbors import KNeighborsClassifier\n"
            "from sklearn.model_selection import train_test_split\n\n"
            "# Age: 20-70, Income: 25,000-200,000\n"
            "np.random.seed(42)\n"
            "n = 200\n"
            "age = np.random.uniform(20, 70, (n, 1))\n"
            "income = np.random.uniform(25000, 200000, (n, 1))\n"
            "X = np.hstack([age, income])\n"
            "y = ((age > 45) & (income < 80000)).astype(int).ravel()\n\n"
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\n"
            "# BUG: KNN computes Euclidean distance without feature scaling!\n"
            "knn = KNeighborsClassifier(n_neighbors=5)\n"
            "knn.fit(X_train, y_train)\n\n"
            "print(f'Unscaled Test Accuracy: {knn.score(X_test, y_test):.3f}')\n"
        ),
        "metrics_log": {
            "Age Variance": "210.4",
            "Income Variance": "2,480,000,000.0",
            "Distance Weight of Income": "99.99%",
            "Distance Weight of Age": "0.01%"
        },
        "hints": [
            "Euclidean distance = sqrt((age1 - age2)^2 + (income1 - income2)^2).",
            "A difference of $5,000 in income will overpower a difference of 30 years in age by millions."
        ],
        "options": [
            "KNN requires setting n_neighbors = 1",
            "Missing Feature Scaling: Large magnitude features dominate Euclidean distance in distance-based algorithms",
            "Age is not a valid numerical feature",
            "KNN cannot perform non-linear classification"
        ],
        "correct_option": 1,
        "explanation": "Distance-based algorithms (KNN, SVM, K-Means) compute Euclidean distance. Without standardization (StandardScaler or MinMaxScaler), features with large numerical ranges completely overpower smaller features.",
        "fix_code_snippet": (
            "# Standardize features before fitting distance-based models:\n"
            "from sklearn.preprocessing import StandardScaler\n"
            "scaler = StandardScaler()\n"
            "X_train_scaled = scaler.fit_transform(X_train)\n"
            "X_test_scaled = scaler.transform(X_test)\n"
            "knn.fit(X_train_scaled, y_train)"
        ),
        "concept_mastered": "Feature Scaling & Distance Metrics in KNN/SVM",
        "xp_reward": 50
    },
    {
        "id": "scenario-vanishing-gradients",
        "title": "The Saturated Sigmoid Deep Network",
        "category": "Deep Learning Bugs",
        "difficulty": "Advanced",
        "description": "An 8-layer deep neural network fails to train. The first 3 layers have zero weight updates and the loss refuses to decrease past epoch 1.",
        "symptoms": [
            "Layer 1-3 Gradient Norm: 0.000001",
            "Layer 7-8 Gradient Norm: 0.450",
            "Training Loss flatlines"
        ],
        "code_snippet": (
            "# ========================================================\n"
            "# pipeline_inspect.py - Deep Multilayer Network\n"
            "# ========================================================\n"
            "import numpy as np\n\n"
            "def sigmoid(z):\n"
            "    return 1.0 / (1.0 + np.exp(-np.clip(z, -15, 15)))\n\n"
            "def sigmoid_derivative(a):\n"
            "    # Maximum derivative of sigmoid is 0.25 (at z=0)!\n"
            "    return a * (1.0 - a)\n\n"
            "# 8-Layer Deep Network using Sigmoid Activations\n"
            "np.random.seed(42)\n"
            "layers = [10, 32, 32, 32, 32, 32, 32, 32, 1]\n"
            "weights = [np.random.randn(layers[i], layers[i+1]) * 1.5 for i in range(len(layers)-1)]\n\n"
            "# Backpropagation gradient product: 0.25^8 = 0.000015\n"
            "print('Multiplying 8 sigmoid derivatives shrinks gradients to zero!')\n"
        ),
        "metrics_log": {
            "Network Depth": "8 Layers",
            "Activation Function": "Sigmoid",
            "Layer 1 Gradients": "1.2e-06",
            "Layer 8 Gradients": "0.38"
        },
        "hints": [
            "What is the maximum derivative value of the Sigmoid function? (Hint: 0.25)",
            "What happens when you multiply (0.25 * 0.25 * 0.25 ...) across 8 layers in the chain rule?"
        ],
        "options": [
            "The network has too many neurons per layer",
            "Vanishing Gradient Problem: Chaining multiple Sigmoid activations causes early layer gradients to shrink exponentially to 0",
            "Sigmoid cannot be differentiated",
            "The learning rate must be negative"
        ],
        "correct_option": 1,
        "explanation": "Sigmoid's derivative has a maximum value of 0.25. In deep networks, the chain rule multiplies these fractions layer by layer (0.25^8 approx 0.000015), causing gradients to vanish and freezing early weights. Use ReLU or GELU activations with He initialization.",
        "fix_code_snippet": (
            "# Use ReLU activations and He/Kaiming weight initialization:\n"
            "def relu(z):\n"
            "    return np.maximum(0, z)\n"
            "# Derivative of ReLU is 1 for positive values, preventing gradient decay!"
        ),
        "concept_mastered": "Vanishing Gradients & Activation Functions",
        "xp_reward": 50
    },
    {
        "id": "scenario-learning-rate-divergence",
        "title": "The Exploding Loss (NaN) Divergence",
        "category": "Optimization & Hyperparameters",
        "difficulty": "Intermediate",
        "description": "During training of a regression model with gradient descent, the loss initially increases from 10 to 1,000,000 and then suddenly becomes NaN.",
        "symptoms": [
            "Epoch 1 Loss: 12.4",
            "Epoch 2 Loss: 894.2",
            "Epoch 3 Loss: 1,420,000.0",
            "Epoch 4 Loss: NaN"
        ],
        "code_snippet": (
            "# ========================================================\n"
            "# pipeline_inspect.py - Gradient Descent Training Loop\n"
            "# ========================================================\n"
            "import numpy as np\n\n"
            "np.random.seed(42)\n"
            "X = 2 * np.random.rand(100, 1)\n"
            "y = 4 + 3 * X + np.random.randn(100, 1)\n\n"
            "w = 0.0\n"
            "b = 0.0\n"
            "# BUG: Learning rate is way too large, overshooting the valley\n"
            "learning_rate = 8.5\n\n"
            "for epoch in range(10):\n"
            "    y_pred = w * X + b\n"
            "    loss = np.mean((y_pred - y) ** 2)\n"
            "    dw = (2 / len(X)) * np.sum((y_pred - y) * X)\n"
            "    db = (2 / len(X)) * np.sum(y_pred - y)\n"
            "    w -= learning_rate * dw\n"
            "    b -= learning_rate * db\n"
            "    print(f'Epoch {epoch}: Loss = {loss:.2f}')\n"
        ),
        "metrics_log": {
            "Learning Rate": "8.5",
            "Final Loss": "NaN",
            "Gradient Magnitude": "Overflow (> 10^308)"
        },
        "hints": [
            "If the step size is larger than the curvature of the loss bowl, what happens to the next step?",
            "Instead of stepping downhill toward the minimum, the weights overshoot to an even higher point on the opposite slope."
        ],
        "options": [
            "The dataset has invalid negative numbers",
            "Exploding Gradient / Divergence: Excessive learning rate causes gradient descent to overshoot the valley and diverge to infinity (NaN)",
            "The bias parameter b must be fixed at 0",
            "NumPy cannot multiply floats"
        ],
        "correct_option": 1,
        "explanation": "An excessively large learning rate causes gradient descent to overshoot the local minimum, landing at a higher loss point on the opposite side of the bowl. Each step becomes exponentially larger until floating point overflow produces NaN.",
        "fix_code_snippet": (
            "# Reduce learning rate and normalize features:\n"
            "learning_rate = 0.01  # Safe step size\n"
            "# Or use adaptive optimizers like Adam"
        ),
        "concept_mastered": "Learning Rate Tuning & Gradient Descent Stability",
        "xp_reward": 50
    },
    {
        "id": "scenario-dead-relu",
        "title": "The Dead ReLU Blackout",
        "category": "Deep Learning Bugs",
        "difficulty": "Advanced",
        "description": "After 50 epochs of training a multilayer perceptron for image classification, the accuracy remains frozen at exactly 10.0% (random guess for 10 classes). Inspect the activation state of the hidden units.",
        "symptoms": [
            "Training Accuracy: 10.00% (Epoch 1 through Epoch 50)",
            "98% of hidden neurons output exactly 0.0 for every training sample",
            "Gradients through ReLU units are permanently 0"
        ],
        "code_snippet": (
            "# ========================================================\n"
            "# pipeline_inspect.py - MLP Hidden Activation Monitor\n"
            "# ========================================================\n"
            "import numpy as np\n\n"
            "np.random.seed(42)\n"
            "n_samples, n_features, n_classes = 500, 20, 10\n"
            "X = np.random.randn(n_samples, n_features)\n"
            "y = np.random.randint(0, n_classes, n_samples)\n\n"
            "# BUG: Initializing biases with large negative numbers pushes all pre-activations into the negative region\n"
            "W1 = np.random.randn(n_features, 64) * 0.01\n"
            "b1 = np.full((1, 64), -10.0)  # Large negative bias initialization!\n\n"
            "W2 = np.random.randn(64, n_classes) * 0.01\n"
            "b2 = np.zeros((1, n_classes))\n\n"
            "# Forward pass\n"
            "Z1 = np.dot(X, W1) + b1\n"
            "A1 = np.maximum(0, Z1)  # ReLU activation\n\n"
            "active_neurons = np.sum(A1 > 0, axis=0)\n"
            "dead_neurons_count = np.sum(active_neurons == 0)\n"
            "print(f'Total hidden units: {64}')\n"
            "print(f'Dead neurons (always 0): {dead_neurons_count} / 64 ({dead_neurons_count/64*100:.1f}%)')\n"
            "print(f'Gradient flowing back through dead ReLUs: 0.0000')\n"
        ),
        "metrics_log": {
            "Hidden Units": 64,
            "Dead Neurons": "64 (100%)",
            "Initial Bias b1": "-10.0",
            "Training Accuracy": "10.00% (Frozen)",
            "Gradient Flow": "0.0000"
        },
        "hints": [
            "What is the gradient of ReLU(z) when z <= 0?",
            "If all inputs to a neuron produce negative pre-activation z, the output is 0 and the derivative is 0.",
            "Once a ReLU unit enters the negative region with zero gradient, it never updates again (Dead ReLU)."
        ],
        "options": [
            "The batch size is too small",
            "Dying ReLU Problem: Large negative bias pushes all activations below zero, extinguishing gradients permanently",
            "The number of classes must be a power of 2",
            "Matrix multiplication cannot use float values"
        ],
        "correct_option": 1,
        "explanation": "When neurons enter the negative regime of ReLU, their activation is 0 and derivative is 0. With zero gradients, weights and biases never update during backpropagation, causing the neuron to die permanently. Fix by initializing biases to small positive values (e.g. 0.01) or using Leaky ReLU / ELU.",
        "fix_code_snippet": (
            "# Fix: Initialize biases with small positive values or use LeakyReLU:\n"
            "b1 = np.full((1, 64), 0.01)  # Positive bias encourages active units\n"
            "# Or use LeakyReLU activation:\n"
            "A1 = np.where(Z1 > 0, Z1, 0.01 * Z1)"
        ),
        "concept_mastered": "Dying ReLU Problem & Activation Initialization",
        "xp_reward": 50
    },
    {
        "id": "scenario-dummy-variable-trap",
        "title": "The Dummy Variable Trap & Multicollinearity",
        "category": "Data Quality",
        "difficulty": "Intermediate",
        "description": "An automated house price predictor yields absurdly huge coefficients (+5.2e+14 and -5.2e+14) for categorical location columns and fails numerical inversion during linear regression.",
        "symptoms": [
            "Condition number of feature matrix: 1.4e+16 (Severely Ill-conditioned)",
            "Location coefficient for 'Urban': +5,248,192,481,200.0",
            "Location coefficient for 'Suburban': +5,248,192,481,194.0",
            "Extreme instability with tiny changes in training data"
        ],
        "code_snippet": (
            "# ========================================================\n"
            "# pipeline_inspect.py - Real Estate Price Predictor\n"
            "# ========================================================\n"
            "import numpy as np\n"
            "import pandas as pd\n"
            "from sklearn.linear_model import LinearRegression\n\n"
            "# 100 Real estate listings with categorical location\n"
            "np.random.seed(42)\n"
            "locations = np.random.choice(['Urban', 'Suburban', 'Rural'], size=100)\n"
            "sqft = np.random.uniform(800, 3500, size=100)\n"
            "price = sqft * 250 + (locations == 'Urban') * 80000 + np.random.randn(100) * 10000\n\n"
            "df = pd.DataFrame({'sqft': sqft, 'location': locations, 'price': price})\n\n"
            "# BUG: One-hot encoding ALL categories alongside the intercept term creates perfect multicollinearity!\n"
            "df_encoded = pd.get_dummies(df, columns=['location'], drop_first=False)\n\n"
            "X = df_encoded.drop(columns=['price'])\n"
            "y = df_encoded['price']\n\n"
            "model = LinearRegression(fit_intercept=True)\n"
            "model.fit(X, y)\n\n"
            "print('Feature Coefficients:')\n"
            "for col, coef in zip(X.columns, model.coef_):\n"
            "    print(f'  {col:20s}: {coef:+.4e}')\n"
        ),
        "metrics_log": {
            "Matrix Condition Number": "1.4e+16",
            "Encoded Columns": "location_Rural, location_Suburban, location_Urban",
            "Intercept": "Enabled (fit_intercept=True)",
            "Determinant of (X^T X)": "0.0 (Singular Matrix)"
        },
        "hints": [
            "location_Rural + location_Suburban + location_Urban = 1.0 for every single row.",
            "If the model also has an intercept column of 1.0, one column is a exact linear combination of the others.",
            "This creates a singular matrix (X^T X) that cannot be inverted uniquely."
        ],
        "options": [
            "LinearRegression requires normalizing price with log1p",
            "The Dummy Variable Trap: Retaining all k one-hot encoded dummy columns with an intercept term causes perfect multicollinearity",
            "Housing square footage must be converted to square meters",
            "The dataset has too many rows for linear algebra"
        ],
        "correct_option": 1,
        "explanation": "The Dummy Variable Trap occurs when k one-hot columns are created for a categorical variable with k categories. Because their sum equals 1, they are perfectly collinear with the intercept term. Fix by setting `drop_first=True` (creating k-1 dummies) or using L2 regularization.",
        "fix_code_snippet": (
            "# Fix by dropping the first category to avoid collinearity:\n"
            "df_encoded = pd.get_dummies(df, columns=['location'], drop_first=True)\n"
            "# Or use Ridge regression which handles multicollinearity stably"
        ),
        "concept_mastered": "Dummy Variable Trap & Multicollinearity in Regression",
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
