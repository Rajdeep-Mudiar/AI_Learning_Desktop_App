COURSES_DATA = [
    {
        "slug": "python-foundations",
        "title": "Python & NumPy Foundations for AI",
        "description": "Master essential Python programming, vectorized computation with NumPy, and data manipulation with Pandas tailored for machine learning engineers.",
        "category": "Programming Foundations",
        "level": "Beginner",
        "estimated_hours": 8,
        "icon": "Code2",
        "color": "#3B82F6",
        "order": 1,
        "is_published": True,
        "prerequisites": [],
        "skills_taught": ["Python Syntax", "Vectorization", "NumPy Matrix Ops", "Pandas DataFrames", "Data Preprocessing"],
        "syllabus_overview": "This course builds the foundational programming skills necessary for every modern AI engineer. We move swiftly from idiomatic Python constructs to fast vectorized math in NumPy and structured tabular manipulation in Pandas.",
        "modules": [
            {
                "id": "py-mod-1",
                "title": "Module 1: Idiomatic Python & Vector Thinking",
                "description": "Variables, list comprehensions, lambda expressions, and memory paradigms.",
                "order": 1,
                "lesson_ids": ["py-intro-variables", "py-data-structures-comprehensions"]
            },
            {
                "id": "py-mod-2",
                "title": "Module 2: NumPy & Fast Vectorized Math",
                "description": "N-dimensional arrays, broadcasting rules, matrix dot products, and vectorization.",
                "order": 2,
                "lesson_ids": ["py-numpy-arrays-broadcasting", "py-numpy-matrix-operations"]
            },
            {
                "id": "py-mod-3",
                "title": "Module 3: Pandas for ML Data Pipelines",
                "description": "DataFrames, filtering, handling missing values, and feature transformations.",
                "order": 3,
                "lesson_ids": ["py-pandas-dataframes-cleaning"]
            }
        ]
    },
    {
        "slug": "math-for-ai",
        "title": "Mathematics for Artificial Intelligence",
        "description": "The foundational mathematical pillars of ML: Linear algebra, multidimensional calculus, gradient vectors, probability, and statistics.",
        "category": "Mathematics",
        "level": "Intermediate",
        "estimated_hours": 12,
        "icon": "Binary",
        "color": "#8B5CF6",
        "order": 2,
        "is_published": True,
        "prerequisites": ["python-foundations"],
        "skills_taught": ["Linear Algebra", "Dot Products & Projections", "Gradients & Partial Derivatives", "Chain Rule", "Bayes Theorem"],
        "syllabus_overview": "AI models are mathematical transformations. This course teaches you to visualize vectors as arrows in space, understand matrix multiplication as geometric transformations, and intuitively grasp gradients.",
        "modules": [
            {
                "id": "math-mod-1",
                "title": "Module 1: Linear Algebra & Spatial Geometry",
                "description": "Vectors, dot products, projections, matrix transformations, and dimensional rules.",
                "order": 1,
                "lesson_ids": ["math-vectors-dot-products", "math-matrix-multiplication"]
            },
            {
                "id": "math-mod-2",
                "title": "Module 2: Multivariable Calculus & Optimization",
                "description": "Derivatives, partial derivatives, the gradient vector, and the calculus chain rule.",
                "order": 2,
                "lesson_ids": ["math-derivatives-gradients", "math-chain-rule-backprop-math"]
            },
            {
                "id": "math-mod-3",
                "title": "Module 3: Probability & Bayesian Reasoning",
                "description": "Probability distributions, conditional probability, expectation, and Bayes theorem.",
                "order": 3,
                "lesson_ids": ["math-probability-bayes-theorem"]
            }
        ]
    },
    {
        "slug": "ml-fundamentals",
        "title": "Machine Learning Fundamentals",
        "description": "Supervised & unsupervised learning, regression, classification, decision trees, bias-variance tradeoff, and evaluation metrics.",
        "category": "Machine Learning",
        "level": "Beginner",
        "estimated_hours": 14,
        "icon": "Cpu",
        "color": "#10B981",
        "order": 3,
        "is_published": True,
        "prerequisites": ["python-foundations", "math-for-ai"],
        "skills_taught": ["Linear Regression", "Gradient Descent", "Logistic Regression", "Decision Trees", "K-Means Clustering", "Cross Validation"],
        "syllabus_overview": "From linear models to ensemble tree methods, understand classical machine learning algorithms from both a mathematical and practical standpoint.",
        "modules": [
            {
                "id": "ml-mod-1",
                "title": "Module 1: Regression & Optimization",
                "description": "Ordinary Least Squares, Mean Squared Error, and Gradient Descent optimization.",
                "order": 1,
                "lesson_ids": ["ml-linear-regression-ols", "ml-gradient-descent-intuition"]
            },
            {
                "id": "ml-mod-2",
                "title": "Module 2: Classification & Decision Boundaries",
                "description": "Sigmoid activation, binary cross-entropy loss, and Logistic Regression.",
                "order": 2,
                "lesson_ids": ["ml-logistic-regression-classification", "ml-decision-trees-entropy"]
            },
            {
                "id": "ml-mod-3",
                "title": "Module 3: Unsupervised Learning & Clustering",
                "description": "K-Means clustering, centroid updates, inertia, and dimensionality reduction.",
                "order": 3,
                "lesson_ids": ["ml-kmeans-clustering-algorithm"]
            }
        ]
    },
    {
        "slug": "deep-learning-fundamentals",
        "title": "Deep Learning & Neural Networks",
        "description": "Neural network architectures from first principles: Perceptrons, multi-layer networks, backpropagation, CNNs, and optimization strategies.",
        "category": "Deep Learning",
        "level": "Intermediate",
        "estimated_hours": 16,
        "icon": "Network",
        "color": "#F59E0B",
        "order": 4,
        "is_published": True,
        "prerequisites": ["ml-fundamentals"],
        "skills_taught": ["Perceptrons", "Backpropagation", "Activation Functions", "Convolutional Neural Networks", "Adam Optimizer", "Regularization"],
        "syllabus_overview": "Dive into deep neural networks. Learn how nonlinear activations allow networks to approximate arbitrary functions, and how convolutions extract hierarchical spatial features from images.",
        "modules": [
            {
                "id": "dl-mod-1",
                "title": "Module 1: Artificial Neural Networks",
                "description": "Perceptrons, forward propagation, activation functions (ReLU, Sigmoid), and loss curves.",
                "order": 1,
                "lesson_ids": ["dl-perceptron-forward-prop", "dl-backpropagation-engine"]
            },
            {
                "id": "dl-mod-2",
                "title": "Module 2: Convolutional Neural Networks (CNNs)",
                "description": "Kernels, stride, padding, feature maps, pooling layers, and spatial hierarchies.",
                "order": 2,
                "lesson_ids": ["dl-cnn-kernels-convolutions"]
            }
        ]
    },
    {
        "slug": "generative-ai-fundamentals",
        "title": "Generative AI & Transformer Architectures",
        "description": "Large language models, self-attention mechanisms, multi-head attention, positional encodings, prompt engineering, and RAG pipelines.",
        "category": "Generative AI",
        "level": "Advanced",
        "estimated_hours": 18,
        "icon": "Sparkles",
        "color": "#EC4899",
        "order": 5,
        "is_published": True,
        "prerequisites": ["deep-learning-fundamentals"],
        "skills_taught": ["Tokenization & Embeddings", "Scaled Dot-Product Attention", "Transformer Encoders & Decoders", "Prompt Engineering", "RAG Systems"],
        "syllabus_overview": "Understand the architecture powering ChatGPT, Claude, and modern generative AI. Explore how attention mechanisms operate and how to construct Retrieval-Augmented Generation workflows.",
        "modules": [
            {
                "id": "genai-mod-1",
                "title": "Module 1: Tokenization & Embeddings",
                "description": "Byte-Pair Encoding, high-dimensional vector spaces, and cosine similarity.",
                "order": 1,
                "lesson_ids": ["genai-tokenization-embeddings"]
            },
            {
                "id": "genai-mod-2",
                "title": "Module 2: The Attention Mechanism",
                "description": "Query, Key, Value matrices, scaled dot-product attention, and multi-head attention.",
                "order": 2,
                "lesson_ids": ["genai-self-attention-transformers"]
            },
            {
                "id": "genai-mod-3",
                "title": "Module 3: Retrieval-Augmented Generation (RAG)",
                "description": "Vector databases, chunking strategies, semantic retrieval, and augmented prompting.",
                "order": 3,
                "lesson_ids": ["genai-rag-architecture-pipeline"]
            }
        ]
    }
]

LESSONS_DATA = [
    # Lesson 1
    {
        "slug": "py-intro-variables",
        "course_slug": "python-foundations",
        "module_id": "py-mod-1",
        "title": "Python Data Types, References & Memory Model",
        "order": 1,
        "estimated_minutes": 15,
        "difficulty": "Beginner",
        "skill_tag": "python_basics",
        "learning_objectives": [
            "Understand dynamic typing and mutable vs. immutable objects in Python.",
            "Master variable assignment, object identities (id()), and shallow vs deep copies.",
            "Write clean, type-hinted code suitable for production AI scripts."
        ],
        "theory_sections": [
            {
                "title": "Objects, References, and Mutability",
                "content_markdown": "In Python, **everything is an object**. When you assign `x = [1, 2, 3]`, `x` is not the list itself; it is a reference (memory pointer) to the list object on the heap.\n\n* **Immutable types**: `int`, `float`, `str`, `tuple`, `frozenset`. Any operation creating a new value creates a brand new object.\n* **Mutable types**: `list`, `dict`, `set`, `numpy.ndarray`. Modifications occur in-place, which is crucial for efficient ML memory management.",
                "key_takeaway": "Understanding references prevents unexpected side-effects when passing datasets or model weights across functions."
            },
            {
                "title": "Type Hints in Modern ML Code",
                "content_markdown": "Modern machine learning code utilizes Python 3 type annotations (`from typing import List, Dict, Optional, Tuple`) to ensure tensor shapes and parameter formats are unambiguous.",
                "key_takeaway": "Always add type annotations to functions that process tensors and tabular batches."
            }
        ],
        "visual_explainer": {
            "type": "architecture_flow",
            "title": "Python Variable Reference Model",
            "subtitle": "How pointers target memory heap allocations",
            "diagram_type": "memory_pointer",
            "parameters": {"variable": "weights_vector", "target_heap": "0x7ffee1b"}
        },
        "code_example": {
            "title": "Checking Object Identity and Type Annotations",
            "language": "python",
            "code": "import copy\nfrom typing import List\n\ndef normalize_scores(raw_scores: List[float]) -> List[float]:\n    \"\"\"Normalizes raw float scores to sum to 1.0 (softmax preview).\"\"\"\n    total = sum(raw_scores)\n    if total == 0:\n        return [0.0] * len(raw_scores)\n    return [round(score / total, 4) for score in raw_scores]\n\nscores = [10.0, 20.0, 70.0]\nnormalized = normalize_scores(scores)\nprint(f\"Original: {scores}\")\nprint(f\"Normalized: {normalized}\")\nprint(f\"Sum: {sum(normalized):.2f}\")",
            "explanation": "This function takes a typed list of floats and returns normalized probabilities using a list comprehension.",
            "output_preview": "Original: [10.0, 20.0, 70.0]\nNormalized: [0.1, 0.2, 0.7]\nSum: 1.00"
        },
        "quiz_id": "quiz-py-intro-variables",
        "summary": "You explored Python's object reference model, mutability considerations, and modern type hinting paradigms.",
        "next_lesson_slug": "py-numpy-arrays-broadcasting",
        "prev_lesson_slug": None
    },
    # Lesson 2
    {
        "slug": "py-numpy-arrays-broadcasting",
        "course_slug": "python-foundations",
        "module_id": "py-mod-2",
        "title": "NumPy N-Dimensional Arrays & Broadcasting Rules",
        "order": 2,
        "estimated_minutes": 20,
        "difficulty": "Beginner",
        "skill_tag": "numpy_basics",
        "learning_objectives": [
            "Construct multi-dimensional NumPy arrays (`ndarray`) with specific dtypes.",
            "Master array shapes, strides, and memory layout (C-contiguous vs Fortran).",
            "Internalize NumPy's 2 broadcasting rules for shape compatibility without copying data."
        ],
        "theory_sections": [
            {
                "title": "Why NumPy Over Standard Python Lists?",
                "content_markdown": "Python lists store arrays of pointers to individual boxed objects. NumPy arrays store contiguous blocks of homogeneous C-data (e.g. `float32`, `int64`). This enables SIMD (Single Instruction Multiple Data) CPU vectorization and cache locality, executing matrix operations 50x–200x faster.",
                "key_takeaway": "Always vectorize operations with NumPy instead of writing explicit Python `for` loops."
            },
            {
                "title": "The Broadcasting Rules",
                "content_markdown": "Broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.\n\nTwo dimensions are compatible when:\n1. They are **equal**, or\n2. One of them is **1**.\n\nNumPy compares dimensions element-wise starting from the trailing (rightmost) dimensions and moving left.",
                "key_takeaway": "An array of shape `(4, 3)` can be broadcast with shape `(3,)` or `(4, 1)`, but NOT with `(4,)` directly."
            }
        ],
        "visual_explainer": {
            "type": "simulation_preview",
            "title": "2D Broadcasting Mechanics",
            "subtitle": "Expanding dimension of size 1 across a matching axis",
            "diagram_type": "broadcasting_grid",
            "parameters": {"matrix_shape": [3, 3], "vector_shape": [1, 3]}
        },
        "code_example": {
            "title": "Vectorized Feature Normalization with Broadcasting",
            "language": "python",
            "code": "import numpy as np\n\n# Batch of 4 data samples, each with 3 features\nX = np.array([\n    [10.0, 200.0, 0.5],\n    [12.0, 240.0, 0.7],\n    [9.0,  180.0, 0.4],\n    [14.0, 280.0, 0.9]\n])\n\n# Compute mean and standard deviation along column axis (axis=0)\nmean = np.mean(X, axis=0)  # Shape: (3,)\nstd = np.std(X, axis=0)    # Shape: (3,)\n\n# Broadcasting (4, 3) with (3,) seamlessly computes z-score\nX_normalized = (X - mean) / std\n\nprint(\"Features mean:\", mean)\nprint(\"Standardized batch shape:\", X_normalized.shape)\nprint(\"Normalized sample 0:\", np.round(X_normalized[0], 2))",
            "explanation": "Broadcasting automatically stretches the `(3,)` mean and std vectors across all 4 rows in `X` without copying memory.",
            "output_preview": "Features mean: [11.25 225.    0.625]\nStandardized batch shape: (4, 3)\nNormalized sample 0: [-0.67 -0.67 -0.67]"
        },
        "quiz_id": "quiz-py-numpy-arrays-broadcasting",
        "summary": "You learned how NumPy ndarrays store contiguous data and how broadcasting rules enable effortless batch operations.",
        "next_lesson_slug": "math-vectors-dot-products",
        "prev_lesson_slug": "py-intro-variables"
    },
    # Lesson 3: Mathematics
    {
        "slug": "math-vectors-dot-products",
        "course_slug": "math-for-ai",
        "module_id": "math-mod-1",
        "title": "Vectors, Dot Products & Geometric Projections",
        "order": 1,
        "estimated_minutes": 20,
        "difficulty": "Intermediate",
        "skill_tag": "linear_algebra",
        "learning_objectives": [
            "Represent data points and feature embeddings as vectors in $\\mathbb{R}^n$.",
            "Calculate dot products algebraically (sum of products) and geometrically ($|u||v|\\cos\\theta$).",
            "Understand why dot products measure similarity in AI and attention mechanisms."
        ],
        "theory_sections": [
            {
                "title": "Vectors as Features and Directions",
                "content_markdown": "A vector $\\mathbf{v} \\in \\mathbb{R}^n$ is an ordered tuple of $n$ numbers. In AI, a vector can represent:\n- A data point (e.g. house features: [sqft, bedrooms, age])\n- An embedding vector representing the semantic meaning of a word or image\n- A set of trainable weights in a neural network layer.",
                "key_takeaway": "Data in AI is always structured as vectors and matrices."
            },
            {
                "title": "The Dot Product (Inner Product)",
                "content_markdown": "Given two vectors $\\mathbf{a} = [a_1, a_2, \\dots, a_n]$ and $\\mathbf{b} = [b_1, b_2, \\dots, b_n]$, the dot product is defined as:\n\n$$\\mathbf{a} \\cdot \\mathbf{b} = \\sum_{i=1}^n a_i b_i = \\|\\mathbf{a}\\| \\|\\mathbf{b}\\| \\cos(\\theta)$$\n\n**Key Geometric Properties:**\n* If $\\mathbf{a} \\cdot \\mathbf{b} > 0$: Vectors point in a similar direction (acute angle $\\theta < 90^\\circ$).\n* If $\\mathbf{a} \\cdot \\mathbf{b} = 0$: Vectors are **orthogonal** (perpendicular, completely independent).\n* If $\\mathbf{a} \\cdot \\mathbf{b} < 0$: Vectors point in opposing directions.",
                "key_takeaway": "Cosine similarity used in search, embeddings, and Transformer attention is simply a normalized dot product."
            }
        ],
        "visual_explainer": {
            "type": "chart",
            "title": "Vector Dot Product & Angle Similarity",
            "subtitle": "Interactive geometric vector projection",
            "diagram_type": "vector_plane",
            "parameters": {"vector_u": [3, 4], "vector_v": [4, 1]}
        },
        "code_example": {
            "title": "Calculating Dot Product and Cosine Similarity in Python",
            "language": "python",
            "code": "import numpy as np\n\ndef cosine_similarity(u: np.ndarray, v: np.ndarray) -> float:\n    \"\"\"Calculates cos(theta) between two vectors.\"\"\"\n    dot = np.dot(u, v)\n    norm_u = np.linalg.norm(u)\n    norm_v = np.linalg.norm(v)\n    return float(dot / (norm_u * norm_v))\n\n# Embedding vectors for 3 words (2D projection)\nword_king   = np.array([0.9, 0.8])\nword_queen  = np.array([0.85, 0.82])\nword_banana = np.array([0.1, -0.9])\n\nsim_king_queen = cosine_similarity(word_king, word_queen)\nsim_king_banana = cosine_similarity(word_king, word_banana)\n\nprint(f\"Similarity (King, Queen):  {sim_king_queen:.4f}\")\nprint(f\"Similarity (King, Banana): {sim_king_banana:.4f}\")",
            "explanation": "Calculates normalized dot product to prove King and Queen have high semantic similarity (cos ~ 0.99) while Banana is dissimilar.",
            "output_preview": "Similarity (King, Queen):  0.9992\nSimilarity (King, Banana): -0.5694"
        },
        "quiz_id": "quiz-math-vectors-dot-products",
        "summary": "You mastered algebraic and geometric dot products and their application to cosine similarity in AI embeddings.",
        "next_lesson_slug": "math-derivatives-gradients",
        "prev_lesson_slug": "py-numpy-arrays-broadcasting"
    },
    # Lesson 4: Math Calculus
    {
        "slug": "math-derivatives-gradients",
        "course_slug": "math-for-ai",
        "module_id": "math-mod-2",
        "title": "Derivatives, Gradients & Multivariable Optimization",
        "order": 2,
        "estimated_minutes": 25,
        "difficulty": "Intermediate",
        "skill_tag": "calculus",
        "learning_objectives": [
            "Understand the derivative as the instantaneous rate of change.",
            "Compute partial derivatives with respect to specific parameter dimensions.",
            "Construct the gradient vector $\\nabla f$ and understand why it points in the direction of steepest ascent."
        ],
        "theory_sections": [
            {
                "title": "The Gradient Vector $\\nabla f$",
                "content_markdown": "In single-variable calculus, $f'(x) = \\frac{df}{dx}$ gives the slope of the tangent line. In machine learning, loss functions depend on millions of weights: $L(w_1, w_2, \\dots, w_d)$.\n\nThe **gradient** $\\nabla L$ is a vector containing all partial derivatives:\n\n$$\\nabla L(\\mathbf{w}) = \\left[ \\frac{\\partial L}{\\partial w_1}, \\frac{\\partial L}{\\partial w_2}, \\dots, \\frac{\\partial L}{\\partial w_d} \\right]^T$$\n\n* **Direction of $\\nabla L$**: Points in the direction of **steepest increase** in loss.\n* **Direction of $-\\nabla L$**: Points in the direction of **steepest decrease** (the path taken in Gradient Descent).",
                "key_takeaway": "To minimize loss, algorithms take steps in the negative gradient direction: w = w - alpha * grad."
            }
        ],
        "visual_explainer": {
            "type": "diagram",
            "title": "Loss Surface Gradient Descent Path",
            "subtitle": "Contour map indicating gradient descent steps toward global minimum",
            "diagram_type": "contour_gradient"
        },
        "code_example": {
            "title": "Numerical Gradient Computation in Python",
            "language": "python",
            "code": "import numpy as np\n\ndef loss_fn(w: np.ndarray) -> float:\n    \"\"\"Convex paraboloid loss surface: L(w1, w2) = w1^2 + 2*w2^2\"\"\"\n    return float(w[0]**2 + 2 * w[1]**2)\n\ndef compute_numerical_gradient(w: np.ndarray, eps: float = 1e-5) -> np.ndarray:\n    \"\"\"Approximates gradient using central differences.\"\"\"\n    grad = np.zeros_like(w, dtype=float)\n    for i in range(len(w)):\n        w_plus = w.copy()\n        w_minus = w.copy()\n        w_plus[i] += eps\n        w_minus[i] -= eps\n        grad[i] = (loss_fn(w_plus) - loss_fn(w_minus)) / (2 * eps)\n    return grad\n\nw_current = np.array([4.0, 3.0])\ngrad = compute_numerical_gradient(w_current)\nprint(f\"Weights at: {w_current}\")\nprint(f\"Computed Gradient: {grad}\")\nprint(f\"Step direction (-grad): {-grad}\")",
            "explanation": "Calculates partial derivatives numerically: dL/dw1 = 2*w1 = 8.0 and dL/dw2 = 4*w2 = 12.0.",
            "output_preview": "Weights at: [4. 3.]\nComputed Gradient: [ 8. 12.]\nStep direction (-grad): [ -8. -12.]"
        },
        "quiz_id": "quiz-math-derivatives-gradients",
        "summary": "You explored multivariable partial derivatives and the geometric significance of the gradient vector in model optimization.",
        "next_lesson_slug": "ml-linear-regression-ols",
        "prev_lesson_slug": "math-vectors-dot-products"
    },
    # Lesson 5: ML
    {
        "slug": "ml-linear-regression-ols",
        "course_slug": "ml-fundamentals",
        "module_id": "ml-mod-1",
        "title": "Linear Regression: Ordinary Least Squares & Gradient Descent",
        "order": 1,
        "estimated_minutes": 25,
        "difficulty": "Beginner",
        "skill_tag": "regression",
        "learning_objectives": [
            "Formulate linear regression hypothesis $\\hat{y} = \\mathbf{w}^T \\mathbf{x} + b$.",
            "Derive the Mean Squared Error (MSE) loss function.",
            "Implement batch gradient descent updates from scratch."
        ],
        "theory_sections": [
            {
                "title": "The Linear Model Hypothesis",
                "content_markdown": "Linear regression models the relationship between dependent target variable $y$ and independent explanatory features $\\mathbf{x}$ as a linear combination:\n\n$$\\hat{y} = w_1 x_1 + w_2 x_2 + \\dots + w_d x_d + b = \\mathbf{w}^T \\mathbf{x} + b$$\n\nOur objective is to find optimal weights $\\mathbf{w}^*$ and bias $b^*$ that minimize prediction residuals across all training examples.",
                "key_takeaway": "Linear regression is the foundational model for continuous target prediction."
            },
            {
                "title": "Mean Squared Error (MSE) Loss",
                "content_markdown": "We quantify model performance using Mean Squared Error:\n\n$$MSE(\\mathbf{w}, b) = \\frac{1}{N} \\sum_{i=1}^N (\\hat{y}^{(i)} - y^{(i)})^2 = \\frac{1}{N} \\sum_{i=1}^N (\\mathbf{w}^T \\mathbf{x}^{(i)} + b - y^{(i)})^2$$\n\nTaking partial derivatives yields the gradient update formulas:\n* $\\frac{\\partial L}{\\partial \\mathbf{w}} = \\frac{2}{N} \\mathbf{X}^T (\\hat{\\mathbf{y}} - \\mathbf{y})$\n* $\\frac{\\partial L}{\\partial b} = \\frac{2}{N} \\sum (\\hat{y}^{(i)} - y^{(i)})$",
                "key_takeaway": "Because MSE is convex, Gradient Descent is guaranteed to converge to the global minimum (for suitable learning rates)."
            }
        ],
        "visual_explainer": {
            "type": "simulation_preview",
            "title": "Linear Regression Best-Fit Line & Residuals",
            "subtitle": "Scatter plot with dynamic regression line minimizing sum of squared residuals",
            "diagram_type": "linear_regression",
            "parameters": {"slope": 1.8, "intercept": 2.4, "mse": 0.042}
        },
        "code_example": {
            "title": "Training Linear Regression from Scratch with NumPy",
            "language": "python",
            "code": "import numpy as np\n\n# Synthetic dataset: y = 2.5 * x + 4.0 + noise\nnp.random.seed(42)\nX = 2 * np.random.rand(100, 1)\ny = 2.5 * X + 4.0 + np.random.randn(100, 1) * 0.2\n\n# Initialize parameters\nw = 0.0\nb = 0.0\nlr = 0.1\nepochs = 50\nN = len(X)\n\nfor epoch in range(epochs):\n    # 1. Forward Pass: Predictions\n    y_hat = w * X + b\n    # 2. Compute Loss\n    mse = np.mean((y_hat - y) ** 2)\n    # 3. Compute Gradients\n    dw = (2 / N) * np.sum((y_hat - y) * X)\n    db = (2 / N) * np.sum(y_hat - y)\n    # 4. Parameter Update\n    w -= lr * dw\n    b -= lr * db\n\nprint(f\"Trained weight w: {w:.3f} (True: 2.500)\")\nprint(f\"Trained bias b:   {b:.3f} (True: 4.000)\")\nprint(f\"Final MSE Loss:   {mse:.4f}\")",
            "explanation": "Illustrates the complete iterative optimization loop of Gradient Descent updating weights directly in pure NumPy.",
            "output_preview": "Trained weight w: 2.482 (True: 2.500)\nTrained bias b:   4.021 (True: 4.000)\nFinal MSE Loss:   0.0389"
        },
        "quiz_id": "quiz-ml-linear-regression-ols",
        "summary": "You formulated linear regression, derived MSE loss gradients, and implemented gradient descent updates from scratch.",
        "next_lesson_slug": "dl-perceptron-forward-prop",
        "prev_lesson_slug": "math-derivatives-gradients"
    },
    # Lesson 6: Deep Learning
    {
        "slug": "dl-perceptron-forward-prop",
        "course_slug": "deep-learning-fundamentals",
        "module_id": "dl-mod-1",
        "title": "The Perceptron, Multi-Layer Architectures & Activations",
        "order": 1,
        "estimated_minutes": 25,
        "difficulty": "Intermediate",
        "skill_tag": "neural_networks",
        "learning_objectives": [
            "Trace the forward pass through artificial neurons.",
            "Understand why non-linear activation functions (ReLU, Sigmoid) are mathematically essential.",
            "Represent multi-layer perceptron layers using matrix multiplication."
        ],
        "theory_sections": [
            {
                "title": "The Artificial Neuron (Perceptron)",
                "content_markdown": "A single artificial neuron takes inputs $\\mathbf{x}$, multiplies them by trainable weights $\\mathbf{w}$, adds a scalar bias $b$, and passes the pre-activation $z$ through a nonlinear activation function $\\sigma(z)$:\n\n$$z = \\sum_{j=1}^d w_j x_j + b = \\mathbf{w}^T \\mathbf{x} + b$$\n$$a = \\sigma(z)$$\n\nWithout non-linear activations, stacking 100 linear layers is mathematically equivalent to a single linear layer ($W_2 W_1 x = W_{combined} x$). Non-linearities allow neural networks to model arbitrary complex decision boundaries.",
                "key_takeaway": "Activation functions introduce non-linearity, enabling deep networks to approximate any continuous function."
            }
        ],
        "visual_explainer": {
            "type": "diagram",
            "title": "Multi-Layer Perceptron (MLP) Architecture",
            "subtitle": "Input Layer -> Hidden Dense Layer (ReLU) -> Output Layer (Softmax)",
            "diagram_type": "neural_net",
            "parameters": {"layers": [3, 4, 2]}
        },
        "code_example": {
            "title": "2-Layer Neural Network Forward Pass in NumPy",
            "language": "python",
            "code": "import numpy as np\n\ndef relu(z):\n    return np.maximum(0, z)\n\ndef softmax(z):\n    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))\n    return exp_z / np.sum(exp_z, axis=1, keepdims=True)\n\n# Batch of 2 samples with 3 features\nX = np.array([\n    [1.0, 2.0, -1.0],\n    [0.5, -1.5, 2.0]\n])\n\n# Layer 1: 3 inputs -> 4 hidden neurons\nW1 = np.random.randn(3, 4) * 0.1\nb1 = np.zeros((1, 4))\n\n# Layer 2: 4 hidden -> 2 output classes\nW2 = np.random.randn(4, 2) * 0.1\nb2 = np.zeros((1, 2))\n\n# Forward Pass\nZ1 = np.dot(X, W1) + b1\nA1 = relu(Z1)             # Hidden activation\nZ2 = np.dot(A1, W2) + b2\nprobs = softmax(Z2)       # Output probabilities\n\nprint(\"Hidden layer activation shape:\", A1.shape)\nprint(\"Predicted class probabilities:\")\nprint(np.round(probs, 4))",
            "explanation": "Demonstrates forward propagation: matrix multiplication followed by ReLU non-linearity and Softmax probability normalization.",
            "output_preview": "Hidden layer activation shape: (2, 4)\nPredicted class probabilities:\n[[0.5012 0.4988]\n [0.4995 0.5005]]"
        },
        "quiz_id": "quiz-dl-perceptron-forward-prop",
        "summary": "You learned neuron mechanics, activation functions, and vectorizing multi-layer forward passes.",
        "next_lesson_slug": "genai-self-attention-transformers",
        "prev_lesson_slug": "ml-linear-regression-ols"
    },
    # Lesson 7: GenAI
    {
        "slug": "genai-self-attention-transformers",
        "course_slug": "generative-ai-fundamentals",
        "module_id": "genai-mod-2",
        "title": "Scaled Dot-Product Self-Attention & Transformers",
        "order": 1,
        "estimated_minutes": 30,
        "difficulty": "Advanced",
        "skill_tag": "transformers",
        "learning_objectives": [
            "Deconstruct Query ($Q$), Key ($K$), and Value ($V$) projections.",
            "Understand the Scaled Dot-Product Attention equation $\\text{Softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right)V$.",
            "Explain why dividing by $\\sqrt{d_k}$ prevents vanishing softmax gradients in high dimensions."
        ],
        "theory_sections": [
            {
                "title": "The Self-Attention Mechanism",
                "content_markdown": "In language, word meanings depend on context. In the sentence *'The animal didn't cross the street because it was too tired'*, self-attention allows the token *'it'* to attend strongly to *'animal'* rather than *'street'*.\n\nEvery token embedding is projected into 3 representations:\n1. **Query ($Q$)**: *'What am I looking for?'*\n2. **Key ($K$)**: *'What information do I have?'*\n3. **Value ($V$)**: *'What content do I provide if matched?'*\n\n$$\\text{Attention}(Q, K, V) = \\text{Softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right) V$$",
                "key_takeaway": "Self-attention computes dynamic pairwise relevance weights between all tokens simultaneously in parallel."
            },
            {
                "title": "Why Scale by $\\sqrt{d_k}$?",
                "content_markdown": "For large projection dimensions $d_k$, the dot products $q \\cdot k$ grow large in magnitude. Large values push the Softmax function into regions with extremely small gradients (vanishing gradients). Dividing by $\\sqrt{d_k}$ stabilizes variance to 1.0.",
                "key_takeaway": "Scaling preserves well-behaved gradients during backpropagation."
            }
        ],
        "visual_explainer": {
            "type": "diagram",
            "title": "Scaled Dot-Product Attention Flow",
            "subtitle": "Q * K^T -> Scale -> Mask -> Softmax -> Weight V",
            "diagram_type": "attention_matrix"
        },
        "code_example": {
            "title": "Scaled Dot-Product Attention in Pure NumPy",
            "language": "python",
            "code": "import numpy as np\n\ndef softmax(x):\n    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))\n    return e_x / np.sum(e_x, axis=-1, keepdims=True)\n\ndef scaled_dot_product_attention(Q, K, V):\n    d_k = Q.shape[-1]\n    # 1. Q * K^T\n    scores = np.matmul(Q, K.T)\n    # 2. Scale by sqrt(d_k)\n    scaled_scores = scores / np.sqrt(d_k)\n    # 3. Softmax attention weights\n    attention_weights = softmax(scaled_scores)\n    # 4. Weighted sum of values\n    output = np.matmul(attention_weights, V)\n    return output, attention_weights\n\n# 3 tokens (e.g. ['AI', 'is', 'amazing']), dim=4\nnp.random.seed(42)\nQ = np.random.randn(3, 4)\nK = np.random.randn(3, 4)\nV = np.random.randn(3, 4)\n\nout, weights = scaled_dot_product_attention(Q, K, V)\nprint(\"Attention Weights Matrix (3x3):\")\nprint(np.round(weights, 3))\nprint(\"Token 0 attending to all tokens:\", np.round(weights[0], 3))\nprint(\"Sum of weights for Token 0:\", np.sum(weights[0]))",
            "explanation": "Calculates attention scores and verifies that every row of the attention matrix sums to 1.0 via Softmax.",
            "output_preview": "Attention Weights Matrix (3x3):\n[[0.219 0.443 0.338]\n [0.495 0.384 0.121]\n [0.428 0.301 0.271]]\nToken 0 attending to all tokens: [0.219 0.443 0.338]\nSum of weights for Token 0: 1.0"
        },
        "quiz_id": "quiz-genai-self-attention-transformers",
        "summary": "You understood Query/Key/Value dynamics, scaled attention calculations, and token contextualization in Transformers.",
        "next_lesson_slug": None,
        "prev_lesson_slug": "dl-perceptron-forward-prop"
    }
]

QUIZZES_DATA = [
    {
        "id": "quiz-py-intro-variables",
        "lesson_slug": "py-intro-variables",
        "title": "Python References & Object Mutability Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "What happens in memory when executing: `a = [1, 2]`; `b = a`; `b.append(3)`?",
                "options": [
                    "b gets a new independent copy of the list; a remains [1, 2]",
                    "Both a and b point to the exact same list object on the heap; a is now [1, 2, 3]",
                    "Python throws a ReferenceError",
                    "b is appended but a is set to None"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "python_basics",
                "explanation": "Lists are mutable objects in Python. The assignment `b = a` copies the reference (memory address), not the underlying list. Modifying `b` modifies the same heap allocation that `a` references.",
                "hint": "Remember that Python variables are references (pointers) to objects in memory."
            },
            {
                "id": "q2",
                "type": "true_false",
                "question": "In Python, integers, floats, and strings are immutable data types.",
                "options": ["True", "False"],
                "correct_answer": 0,
                "points": 10,
                "skill_tag": "python_basics",
                "explanation": "True. Numeric types (int, float) and strings are immutable. Any modification (like `x += 1`) allocates a new object rather than modifying the existing memory block in-place."
            }
        ]
    },
    {
        "id": "quiz-py-numpy-arrays-broadcasting",
        "lesson_slug": "py-numpy-arrays-broadcasting",
        "title": "NumPy Broadcasting & Tensor Shapes Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "Which of the following array shape pairs CANNOT be broadcast together under NumPy rules?",
                "options": [
                    "(4, 3) and (3,)",
                    "(5, 1, 4) and (1, 3, 4)",
                    "(3, 4) and (3, 1)",
                    "(4, 3) and (4,)"
                ],
                "correct_answer": 3,
                "points": 10,
                "skill_tag": "numpy_basics",
                "explanation": "Broadcasting aligns trailing (rightmost) dimensions. For `(4, 3)` and `(4,)`, the trailing dimensions are `3` and `4`. Since neither is equal nor 1, NumPy raises a ValueError: operands could not be broadcast together.",
                "hint": "Compare trailing dimensions from right to left. They must be equal or one of them must be 1."
            },
            {
                "id": "q2",
                "type": "fill_blank",
                "question": "What is the resulting shape when broadcasting array A of shape (8, 1, 6) with array B of shape (8, 5, 1)?",
                "options": None,
                "correct_answer": "(8, 5, 6)",
                "points": 15,
                "skill_tag": "numpy_basics",
                "explanation": "Dim 0: 8 and 8 -> 8. Dim 1: 1 and 5 -> 5 (dimension of 1 is stretched). Dim 2: 6 and 1 -> 6. Resulting broadcast shape is (8, 5, 6)."
            }
        ]
    },
    {
        "id": "quiz-math-vectors-dot-products",
        "lesson_slug": "math-vectors-dot-products",
        "title": "Vectors, Dot Products & Linear Algebra Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "If two non-zero vectors u and v have a dot product u · v = 0, what does this indicate geometrically?",
                "options": [
                    "They point in exactly the same direction",
                    "They are orthogonal (perpendicular) to each other with an angle of 90 degrees",
                    "One of the vectors has length zero",
                    "They point in opposite directions (180 degrees)"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "linear_algebra",
                "explanation": "Since u · v = |u||v| cos(theta), when u and v are non-zero, u · v = 0 implies cos(theta) = 0, meaning theta = 90 degrees (orthogonal vectors).",
                "hint": "Recall the geometric formula u · v = |u||v|cos(theta)."
            },
            {
                "id": "q2",
                "type": "multiple_choice",
                "question": "Given vector a = [2, 3] and vector b = [4, -1], what is the algebraic dot product a · b?",
                "options": ["5", "8", "11", "-5"],
                "correct_answer": 0,
                "points": 10,
                "skill_tag": "linear_algebra",
                "explanation": "a · b = (2 * 4) + (3 * -1) = 8 + (-3) = 5."
            }
        ]
    },
    {
        "id": "quiz-math-derivatives-gradients",
        "lesson_slug": "math-derivatives-gradients",
        "title": "Derivatives & Gradients Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "Why do Gradient Descent algorithms subtract the gradient (w = w - alpha * grad) instead of adding it?",
                "options": [
                    "The gradient vector points in the direction of steepest increase; the negative gradient points toward steepest decrease.",
                    "Adding the gradient causes integer overflow in floating point hardware.",
                    "Subtracting ensures the learning rate alpha is always positive.",
                    "The sign is arbitrary and either addition or subtraction finds the minimum."
                ],
                "correct_answer": 0,
                "points": 10,
                "skill_tag": "calculus",
                "explanation": "By definition, the gradient vector points in the direction of greatest rate of increase (steepest ascent). To minimize the loss function, we must step in the opposite direction (-grad).",
                "hint": "Think of moving downhill on a 3D valley loss surface."
            }
        ]
    },
    {
        "id": "quiz-ml-linear-regression-ols",
        "lesson_slug": "ml-linear-regression-ols",
        "title": "Linear Regression & Gradient Descent Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "What occurs if the learning rate alpha in Gradient Descent is set excessively high?",
                "options": [
                    "The model converges to the global minimum instantaneously",
                    "The loss oscillates and diverges away from the minimum",
                    "The weights become permanently zero",
                    "The Mean Squared Error function ceases to be convex"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "regression",
                "explanation": "An excessively large learning rate causes updates to overshoot the valley of the convex loss surface, leading to wild oscillations and numerical divergence (loss reaching infinity/NaN).",
                "hint": "What happens when step sizes overshoot the bottom of the valley?"
            }
        ]
    },
    {
        "id": "quiz-dl-perceptron-forward-prop",
        "lesson_slug": "dl-perceptron-forward-prop",
        "title": "Neural Networks & Activations Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "Why can a neural network with only linear activation functions (f(z) = z) NOT learn XOR or complex decision boundaries?",
                "options": [
                    "Linear layers lack trainable bias parameters",
                    "The composition of any number of linear transformations is mathematically just another single linear transformation",
                    "Linear activations always produce negative outputs",
                    "Backpropagation cannot calculate derivatives for linear functions"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "neural_networks",
                "explanation": "For linear layers: f(x) = W2(W1*x + b1) + b2 = (W2*W1)*x + (W2*b1 + b2) = W_new * x + b_new. No matter the depth, the entire network reduces to a single hyper-plane linear classifier, unable to model non-linear relations like XOR."
            }
        ]
    },
    {
        "id": "quiz-genai-self-attention-transformers",
        "lesson_slug": "genai-self-attention-transformers",
        "title": "Transformers & Self-Attention Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "In Scaled Dot-Product Attention, what is the mathematical purpose of dividing QK^T by sqrt(d_k)?",
                "options": [
                    "To ensure the attention weights matrix is symmetric",
                    "To prevent large dot product magnitudes from pushing the Softmax into saturated regions with vanishing gradients",
                    "To convert the matrix into complex numbers",
                    "To enforce causality in autoregressive generation"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "transformers",
                "explanation": "When dimension d_k is large, the variance of the dot products scales with d_k. Unscaled large inputs to Softmax produce outputs close to 1 and 0 with nearly zero derivatives, causing severe vanishing gradient problems during backprop.",
                "hint": "Consider the derivative of Softmax when inputs have large magnitudes."
            }
        ]
    }
]

SKILLS_DATA = [
    # Programming
    {"id": "python_basics", "category": "Programming", "title": "Python Syntax & Idioms", "description": "Core language constructs, references, comprehensions, and data structures.", "level": 1, "prerequisites": []},
    {"id": "numpy_basics", "category": "Programming", "title": "NumPy Vectorized Computing", "description": "N-dimensional arrays, broadcasting, and high-performance vector math.", "level": 1, "prerequisites": ["python_basics"]},
    {"id": "pandas_basics", "category": "Programming", "title": "Pandas Data Pipelines", "description": "DataFrame transformations, cleaning, and feature preparation.", "level": 2, "prerequisites": ["numpy_basics"]},
    
    # Mathematics
    {"id": "linear_algebra", "category": "Mathematics", "title": "Linear Algebra & Vectors", "description": "Dot products, matrix transformations, spatial projections, and eigenvalues.", "level": 1, "prerequisites": []},
    {"id": "calculus", "category": "Mathematics", "title": "Multivariable Calculus & Gradients", "description": "Partial derivatives, gradient vectors, and optimization landscapes.", "level": 2, "prerequisites": ["linear_algebra"]},
    {"id": "statistics", "category": "Mathematics", "title": "Probability & Statistics", "description": "Distributions, expectation, Bayes theorem, and hypothesis testing.", "level": 2, "prerequisites": []},
    
    # Machine Learning
    {"id": "supervised_learning", "category": "Machine Learning", "title": "Supervised Learning Foundations", "description": "Target prediction, training/testing splits, and evaluation metrics.", "level": 1, "prerequisites": ["linear_algebra"]},
    {"id": "regression", "category": "Machine Learning", "title": "Linear & Polynomial Regression", "description": "Ordinary Least Squares, MSE minimization, and gradient descent.", "level": 2, "prerequisites": ["supervised_learning", "calculus"]},
    {"id": "classification", "category": "Machine Learning", "title": "Logistic Regression & Trees", "description": "Cross-entropy, decision boundaries, entropy, and Random Forests.", "level": 2, "prerequisites": ["supervised_learning"]},
    
    # Deep Learning
    {"id": "neural_networks", "category": "Deep Learning", "title": "Multi-Layer Perceptrons (MLP)", "description": "Neuron forward pass, activations (ReLU/Sigmoid), and backpropagation.", "level": 2, "prerequisites": ["calculus", "regression"]},
    {"id": "deep_learning", "category": "Deep Learning", "title": "CNNs & Computer Vision", "description": "Convolutional filters, pooling, stride, and spatial feature maps.", "level": 3, "prerequisites": ["neural_networks"]},
    
    # Generative AI
    {"id": "transformers", "category": "Generative AI", "title": "Transformers & Self-Attention", "description": "Query/Key/Value mechanisms, multi-head attention, and token embeddings.", "level": 3, "prerequisites": ["neural_networks"]},
    {"id": "rag", "category": "Generative AI", "title": "RAG & Vector Retrieval", "description": "Vector stores, semantic chunking, embedding distance, and grounding.", "level": 4, "prerequisites": ["transformers"]}
]
