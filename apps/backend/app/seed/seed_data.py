COURSES_DATA = [
    {
        "slug": "python-foundations",
        "title": "Python & NumPy Foundations for AI",
        "description": "Master essential Python programming, fast matrix math with NumPy, and structured data manipulation with Pandas tailored for machine learning engineers.",
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
                "title": "Module 1: Everyday Python & Memory Basics",
                "description": "Variables, memory references, list comprehensions, and practical data structures.",
                "order": 1,
                "lesson_ids": ["py-intro-variables", "py-data-structures-comprehensions"]
            },
            {
                "id": "py-mod-2",
                "title": "Module 2: NumPy & Fast Array Math",
                "description": "Arrays, broadcasting rules, matrix dot products, and speeding up code without loops.",
                "order": 2,
                "lesson_ids": ["py-numpy-arrays-broadcasting", "py-numpy-matrix-operations"]
            },
            {
                "id": "py-mod-3",
                "title": "Module 3: Pandas for AI Data Cleaning",
                "description": "DataFrames, filtering, handling missing values, and preparing real datasets.",
                "order": 3,
                "lesson_ids": ["py-pandas-dataframes-cleaning"]
            }
        ]
    },
    {
        "slug": "math-for-ai",
        "title": "Mathematics for Artificial Intelligence",
        "description": "The foundational math pillars of AI explained simply: Vectors, matrices, slope derivatives, gradients, and probability with real-world intuition.",
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
                "title": "Module 1: Vectors & Geometric Similarity",
                "description": "Vectors, dot products, projections, and measuring similarity between data points.",
                "order": 1,
                "lesson_ids": ["math-vectors-dot-products", "math-matrix-multiplication"]
            },
            {
                "id": "math-mod-2",
                "title": "Module 2: Derivatives & Finding the Best Path",
                "description": "Slopes, partial derivatives, and understanding the gradient vector as a compass.",
                "order": 2,
                "lesson_ids": ["math-derivatives-gradients", "math-chain-rule-backprop-math"]
            },
            {
                "id": "math-mod-3",
                "title": "Module 3: Probability & Smart Guessing",
                "description": "Probabilities, odds, and using Bayes Theorem to update predictions with new evidence.",
                "order": 3,
                "lesson_ids": ["math-probability-bayes-theorem"]
            }
        ]
    },
    {
        "slug": "ml-fundamentals",
        "title": "Machine Learning Fundamentals",
        "description": "Learn how computers learn from data: Linear regression, classification, decision trees, evaluating models, and clustering.",
        "category": "Machine Learning",
        "level": "Beginner",
        "estimated_hours": 14,
        "icon": "Cpu",
        "color": "#10B981",
        "order": 3,
        "is_published": True,
        "prerequisites": ["python-foundations", "math-for-ai"],
        "skills_taught": ["Linear Regression", "Gradient Descent", "Logistic Regression", "Decision Trees", "K-Means Clustering", "Cross Validation"],
        "syllabus_overview": "From linear models to decision trees, understand classical machine learning algorithms from both an intuitive and hands-on coding standpoint.",
        "modules": [
            {
                "id": "ml-mod-1",
                "title": "Module 1: Predicting Numbers with Lines",
                "description": "Fitting lines to data, calculating errors, and walking down the loss slope.",
                "order": 1,
                "lesson_ids": ["ml-linear-regression-ols", "ml-gradient-descent-intuition"]
            },
            {
                "id": "ml-mod-2",
                "title": "Module 2: Classifying Yes / No & Trees",
                "description": "Logistic regression, S-curves, asking 20 questions with decision trees.",
                "order": 2,
                "lesson_ids": ["ml-logistic-regression-classification", "ml-decision-trees-entropy"]
            },
            {
                "id": "ml-mod-3",
                "title": "Module 3: Finding Natural Groups (Clustering)",
                "description": "K-Means clustering, grouping unlabeled data, and finding patterns.",
                "order": 3,
                "lesson_ids": ["ml-kmeans-clustering-algorithm"]
            }
        ]
    },
    {
        "slug": "deep-learning-fundamentals",
        "title": "Deep Learning & Neural Networks",
        "description": "How neural networks think: Artificial neurons, forward thinking, learning backwards with backpropagation, and image recognition with CNNs.",
        "category": "Deep Learning",
        "level": "Intermediate",
        "estimated_hours": 16,
        "icon": "Network",
        "color": "#0EA5E9",
        "order": 4,
        "is_published": True,
        "prerequisites": ["ml-fundamentals"],
        "skills_taught": ["Multi-Layer Perceptrons", "Activation Functions", "Backpropagation", "Convolutional Neural Nets", "PyTorch Basics"],
        "syllabus_overview": "Deep learning allows computers to recognize images, translate languages, and beat chess grandmasters. Learn how networks build representations layer by layer.",
        "modules": [
            {
                "id": "dl-mod-1",
                "title": "Module 1: Artificial Neurons & Layers",
                "description": "How a neuron fires, combining inputs with weights, and activation functions.",
                "order": 1,
                "lesson_ids": ["dl-perceptron-forward-prop", "dl-activation-functions"]
            },
            {
                "id": "dl-mod-2",
                "title": "Module 2: Backpropagation (How Networks Learn)",
                "description": "Sending error feedback backwards through the network to tweak weights.",
                "order": 2,
                "lesson_ids": ["dl-backpropagation-calculus"]
            },
            {
                "id": "dl-mod-3",
                "title": "Module 3: Computer Vision with CNNs",
                "description": "Sliding filters over images to detect edges, curves, eyes, and complex objects.",
                "order": 3,
                "lesson_ids": ["dl-cnn-convolution-pooling"]
            }
        ]
    },
    {
        "slug": "generative-ai-fundamentals",
        "title": "Generative AI, Transformers & LLMs",
        "description": "How modern AI like ChatGPT works: Word tokens, embeddings, the Transformer self-attention spotlight, and building RAG applications.",
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
                "title": "Module 1: Words as Numbers (Tokens & Embeddings)",
                "description": "How AI reads text, turning words into coordinate maps where similar words sit together.",
                "order": 1,
                "lesson_ids": ["genai-tokenization-embeddings"]
            },
            {
                "id": "genai-mod-2",
                "title": "Module 2: The Attention Mechanism",
                "description": "Queries, Keys, Values, and connecting related words across long sentences.",
                "order": 2,
                "lesson_ids": ["genai-self-attention-transformers"]
            },
            {
                "id": "genai-mod-3",
                "title": "Module 3: Retrieval-Augmented Generation (RAG)",
                "description": "Connecting your AI to custom documents and databases to answer questions accurately.",
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
            "Understand how Python stores values and assigns variables in memory.",
            "Learn the difference between immutable items (numbers, strings) and mutable items (lists, arrays).",
            "Write clean type-annotated code suitable for machine learning scripts."
        ],
        "theory_sections": [
            {
                "title": "Variables Are Name Tags, Not Boxes",
                "content_markdown": "In Python, **variables act like sticky name tags attached to objects in memory** rather than physical boxes holding values.\n\nWhen you write `x = [1, 2, 3]`, Python creates a list `[1, 2, 3]` in memory and sticks the label `x` on it. If you then write `y = x`, you simply stick a second label `y` on the exact same list!\n\n* **Immutable types** (cannot be altered in-place): `int`, `float`, `str`, `tuple`. If you change `x = 5` to `x = 6`, Python creates a new number `6` and moves your name tag.\n* **Mutable types** (can be altered in-place): `list`, `dict`, `set`, `numpy.ndarray`. Modifying a list with `x.append(4)` changes the object directly in memory for all variables pointing to it.",
                "key_takeaway": "Remember that sharing lists or model weight arrays across functions means any change will affect the original data unless you explicitly copy it."
            },
            {
                "title": "Type Hints for AI Engineering",
                "content_markdown": "In modern AI code, adding type hints tells your team (and editor) what type of data each function expects:\n\n```python\nfrom typing import List\n\ndef calculate_average(scores: List[float]) -> float:\n    return sum(scores) / len(scores)\n```\n\nThis makes working with complex batches of images, tokens, and matrix dimensions clear and bug-free.",
                "key_takeaway": "Use type hints like List[float] or np.ndarray so you always know what shapes and types your functions are processing."
            }
        ],
        "visual_explainer": {
            "type": "architecture_flow",
            "title": "Python Variable Reference Model",
            "subtitle": "How variable name tags point to heap memory",
            "diagram_type": "memory_pointer",
            "parameters": {"variable": "weights_vector", "target_heap": "0x7ffee1b"}
        },
        "code_example": {
            "title": "Checking Object Memory Identity in Python",
            "language": "python",
            "code": "import copy\nfrom typing import List\n\ndef normalize_scores(raw_scores: List[float]) -> List[float]:\n    \"\"\"Calculates simple percentages from a list of raw scores.\"\"\"\n    total = sum(raw_scores)\n    if total == 0:\n        return [0.0] * len(raw_scores)\n    return [round(score / total, 2) for score in raw_scores]\n\nscores = [10.0, 20.0, 70.0]\npercentages = normalize_scores(scores)\nprint(f\"Raw Scores:   {scores}\")\nprint(f\"Percentages:  {percentages}\")\nprint(f\"Total Check:  {sum(percentages):.2f}\")",
            "explanation": "This example normalizes a list of scores so they represent clear probabilities between 0.0 and 1.0.",
            "output_preview": "Raw Scores:   [10.0, 20.0, 70.0]\nPercentages:  [0.1, 0.2, 0.7]\nTotal Check:  1.00"
        },
        "quiz_id": "quiz-py-intro-variables",
        "summary": "You explored how Python variables point to memory and how mutability affects data manipulation.",
        "next_lesson_slug": "py-numpy-arrays-broadcasting",
        "prev_lesson_slug": None
    },
    # Lesson 2
    {
        "slug": "py-numpy-arrays-broadcasting",
        "course_slug": "python-foundations",
        "module_id": "py-mod-2",
        "title": "NumPy Arrays & Fast Broadcasting",
        "order": 2,
        "estimated_minutes": 20,
        "difficulty": "Beginner",
        "skill_tag": "numpy_basics",
        "learning_objectives": [
            "Learn why NumPy arrays are 100x faster than standard Python lists.",
            "Understand array shapes (rows, columns, dimensions).",
            "Master Broadcasting: Doing math on arrays of different sizes without loops."
        ],
        "theory_sections": [
            {
                "title": "Why Is NumPy So Fast?",
                "content_markdown": "Standard Python lists are flexible but slow because each number is wrapped in a full Python object stored across scattered memory addresses.\n\n**NumPy arrays (`ndarray`) pack numbers side-by-side in raw computer memory**, like books lined up neatly on a bookshelf. This allows your computer processor to calculate thousands of numbers in a single clock cycle (SIMD vectorization), making matrix math **50x to 200x faster** than a Python `for` loop.",
                "key_takeaway": "In machine learning, always use NumPy vectorized operations instead of writing loops over data rows."
            },
            {
                "title": "The Magic of Broadcasting",
                "content_markdown": "Broadcasting is NumPy's ability to perform math between arrays of different shapes automatically.\n\n**Analogy**: Imagine you have a shopping receipt with 10 item prices in a column. If you want to add 5% sales tax to every item, you don't need a table of 10 tax rates—you just multiply the whole column by `1.05`! NumPy automatically 'stretches' the single number across all 10 rows.\n\n**The Rule**: Two dimensions are compatible when:\n1. They have the **exact same size**, OR\n2. One of them is **1** (NumPy will stretch the 1 to match the other size).",
                "key_takeaway": "Broadcasting allows you to normalize entire datasets with a single line: (X - mean) / std."
            }
        ],
        "visual_explainer": {
            "type": "simulation_preview",
            "title": "2D Broadcasting Mechanics",
            "subtitle": "Stretching a 1D vector across matching rows",
            "diagram_type": "broadcasting_grid",
            "parameters": {"matrix_shape": [3, 3], "vector_shape": [1, 3]}
        },
        "code_example": {
            "title": "Standardizing Data Features with Broadcasting",
            "language": "python",
            "code": "import numpy as np\n\n# 4 House listings: [Square Footage, Bedrooms, Age in Years]\nhouses = np.array([\n    [1200.0, 2.0, 10.0],\n    [1800.0, 3.0, 5.0],\n    [2400.0, 4.0, 15.0],\n    [3000.0, 5.0, 2.0]\n])\n\n# Calculate average of each column\ncolumn_averages = np.mean(houses, axis=0)\n\n# Center the data around 0 by subtracting column averages\ncentered_houses = houses - column_averages\n\nprint(\"Average for each feature:\", column_averages)\nprint(\"Centered houses:\\n\", centered_houses)",
            "explanation": "NumPy stretches the 3-element average vector across all 4 houses automatically without needing any loop.",
            "output_preview": "Average for each feature: [2100.    3.5    8. ]\nCentered houses:\n [[-900.   -1.5   2. ]\n  [-300.   -0.5  -3. ]\n  [ 300.    0.5   7. ]\n  [ 900.    1.5  -6. ]]"
        },
        "quiz_id": "quiz-py-numpy-arrays-broadcasting",
        "summary": "You learned how NumPy arrays accelerate AI computations and how broadcasting handles multi-dimensional math seamlessly.",
        "next_lesson_slug": "math-vectors-dot-products",
        "prev_lesson_slug": "py-intro-variables"
    },
    # Lesson 3: Math
    {
        "slug": "math-vectors-dot-products",
        "course_slug": "math-for-ai",
        "module_id": "math-mod-1",
        "title": "Vectors, Dot Products & Measuring Similarity",
        "order": 1,
        "estimated_minutes": 20,
        "difficulty": "Intermediate",
        "skill_tag": "linear_algebra",
        "learning_objectives": [
            "Understand vectors as lists of numbers representing features or directions in space.",
            "Calculate the dot product step-by-step: multiply matching elements and add them up.",
            "Learn how dot products measure similarity between search queries, movies, or words."
        ],
        "theory_sections": [
            {
                "title": "What is a Vector?",
                "content_markdown": "A **vector** is simply an ordered list of numbers that describes an object's features or a direction in space.\n\n**Real-World Example**: A house can be represented as a 3-element vector:\n\n$$House = [2000, 3, 2]$$\n\nWhere `2000` is square feet, `3` is bedrooms, and `2` is bathrooms. In AI, words, images, and user preferences are all converted into vectors so math algorithms can compare them.",
                "key_takeaway": "Everything in AI—from words to pictures—is converted into a vector of numbers."
            },
            {
                "title": "The Dot Product: Measuring Similarity",
                "content_markdown": "The **dot product** is the most important operation in AI. You calculate it in two simple steps:\n1. Multiply matching items from two vectors together.\n2. Sum up all the products into one final number.\n\n$$u · v = (u_1 × v_1) + (u_2 × v_2) + ... + (u_n × v_n)$$\n\n**Example Calculation**:\nIf User A's movie taste is `[5, 1]` (loves Action, dislikes Romance) and Movie X is `[4, 0]` (high Action, no Romance):\n\n$$Score = (5 × 4) + (1 × 0) = 20 + 0 = 20$$\n\n* **Positive Dot Product**: Vectors point in a similar direction (strong match!).\n* **Zero (0) Dot Product**: Vectors are perpendicular / completely independent.\n* **Negative Dot Product**: Vectors point in opposite directions.",
                "key_takeaway": "Dot products power recommendation engines, search algorithms, and Transformer self-attention by checking how well two items align."
            }
        ],
        "visual_explainer": {
            "type": "chart",
            "title": "Vector Dot Product & Angle Similarity",
            "subtitle": "Interactive vector alignment in 2D space",
            "diagram_type": "vector_plane",
            "parameters": {"vector_u": [3, 4], "vector_v": [4, 1]}
        },
        "code_example": {
            "title": "Measuring Similarity Between Words Using Vectors",
            "language": "python",
            "code": "import numpy as np\n\ndef cosine_similarity(u: np.ndarray, v: np.ndarray) -> float:\n    \"\"\"Calculates how closely two vectors align (1.0 = identical match).\"\"\"\n    dot = np.dot(u, v)\n    length_u = np.linalg.norm(u)\n    length_v = np.linalg.norm(v)\n    return float(dot / (length_u * length_v))\n\n# 2D Word embeddings\nword_king   = np.array([0.9, 0.8])\nword_queen  = np.array([0.85, 0.82])\nword_banana = np.array([0.1, -0.9])\n\nsim_royals = cosine_similarity(word_king, word_queen)\nsim_fruit  = cosine_similarity(word_king, word_banana)\n\nprint(f\"Similarity (King, Queen):  {sim_royals:.4f} (Almost Identical!)\")\nprint(f\"Similarity (King, Banana): {sim_fruit:.4f} (Unrelated / Opposite)\")",
            "explanation": "Calculates cosine similarity to demonstrate that words with related concepts point in the same direction.",
            "output_preview": "Similarity (King, Queen):  0.9992 (Almost Identical!)\nSimilarity (King, Banana): -0.5694 (Unrelated / Opposite)"
        },
        "quiz_id": "quiz-math-vectors-dot-products",
        "summary": "You mastered vectors and learned how dot products compare similarity between data points.",
        "next_lesson_slug": "math-derivatives-gradients",
        "prev_lesson_slug": "py-numpy-arrays-broadcasting"
    },
    # Lesson 4: Math Calculus
    {
        "slug": "math-derivatives-gradients",
        "course_slug": "math-for-ai",
        "module_id": "math-mod-2",
        "title": "Derivatives, Slopes & The Gradient Compass",
        "order": 2,
        "estimated_minutes": 25,
        "difficulty": "Intermediate",
        "skill_tag": "calculus",
        "learning_objectives": [
            "Understand a derivative as a slope measuring how quickly an output changes.",
            "Learn what a partial derivative is (changing one setting while holding others still).",
            "Understand the Gradient as a compass that points uphill, while negative gradient points downhill."
        ],
        "theory_sections": [
            {
                "title": "What is a Derivative?",
                "content_markdown": "A **derivative** is simply the slope of a curve at a single point.\n\n**Everyday Analogy**: If you are driving a car and glance at your speedometer, it tells you your rate of change right now (e.g. 60 mph). In machine learning, the derivative tells us: *'If I nudge weight setting w by a tiny bit, will the model's error go UP or DOWN?'*",
                "key_takeaway": "Derivatives tell us which direction to tweak our model settings to reduce prediction mistakes."
            },
            {
                "title": "The Gradient: The Compass of AI",
                "content_markdown": "When an AI model has multiple weight parameters ($w_1, w_2, w_3$), we compute the partial derivative for each one.\n\nThe collection of all these slopes in a single list is called the **Gradient** ($\nabla L$):\n\n$$\\text{Gradient} = [\\text{Slope for } w_1, \\text{Slope for } w_2, \\dots, \\text{Slope for } w_n]$$\n\n**The Golden Rule of Gradient Descent**:\n* **The Gradient points UPHILL** (toward higher error/mistakes).\n* **The Negative Gradient points DOWNHILL** (toward minimum error and best accuracy!).",
                "key_takeaway": "To train an AI model, we take small steps downhill in the opposite direction of the gradient: w_new = w_old - learning_rate * gradient."
            }
        ],
        "visual_explainer": {
            "type": "diagram",
            "title": "Loss Surface Gradient Descent Path",
            "subtitle": "Stepping downhill toward the lowest prediction error",
            "diagram_type": "contour_gradient"
        },
        "code_example": {
            "title": "Computing Slopes and Stepping Downhill in Python",
            "language": "python",
            "code": "import numpy as np\n\n# Error function: Error = (w - 3)^2\n# The minimum error happens at w = 3.0\ndef error_fn(w: float) -> float:\n    return (w - 3.0) ** 2\n\ndef derivative_slope(w: float) -> float:\n    # Derivative of (w - 3)^2 is 2 * (w - 3)\n    return 2.0 * (w - 3.0)\n\n# Start with an incorrect guess for w\nw = 10.0\nlearning_rate = 0.2\n\nprint(f\"Starting weight: {w}, Error: {error_fn(w):.2f}\")\nfor step in range(5):\n    slope = derivative_slope(w)\n    w = w - learning_rate * slope\n    print(f\"Step {step+1}: Slope={slope:.2f}, New w={w:.2f}, Error={error_fn(w):.2f}\")",
            "explanation": "Shows how stepping in the opposite direction of the slope automatically brings w closer to the ideal target (3.0).",
            "output_preview": "Starting weight: 10.0, Error: 49.00\nStep 1: Slope=14.00, New w=7.20, Error=17.64\nStep 2: Slope=8.40, New w=5.52, Error=6.35\nStep 3: Slope=5.04, New w=4.51, Error=2.29\nStep 4: Slope=3.02, New w=3.91, Error=0.82\nStep 5: Slope=1.81, New w=3.54, Error=0.30"
        },
        "quiz_id": "quiz-math-derivatives-gradients",
        "summary": "You understood derivatives as slopes and learned why algorithms step downhill using the negative gradient.",
        "next_lesson_slug": "ml-linear-regression-ols",
        "prev_lesson_slug": "math-vectors-dot-products"
    },
    # Lesson 5: ML
    {
        "slug": "ml-linear-regression-ols",
        "course_slug": "ml-fundamentals",
        "module_id": "ml-mod-1",
        "title": "Linear Regression: Finding the Best-Fit Line",
        "order": 1,
        "estimated_minutes": 25,
        "difficulty": "Beginner",
        "skill_tag": "regression",
        "learning_objectives": [
            "Learn the linear prediction formula: Prediction = (Weight × Feature) + Bias.",
            "Understand Mean Squared Error (MSE) as the average squared mistake.",
            "Train a model by iteratively nudging weights to minimize error."
        ],
        "theory_sections": [
            {
                "title": "The Core Linear Equation",
                "content_markdown": "Linear regression is the simplest way to predict a number (like price, temperature, or sales).\n\n$$y_{predicted} = (w · x) + b$$\n\n* $x$ = Input Feature (e.g. Square footage of a house)\n* $w$ = Weight / Multiplier (e.g. Cost per square foot)\n* $b$ = Bias / Starting Baseline (e.g. Base land cost)\n* $y$ = Final Prediction (e.g. Estimated House Price)\n\n**Intuition**: The goal of training is simply finding the best $w$ and $b$ so the line passes right through the middle of your training data points.",
                "key_takeaway": "Linear regression models relationships as straight lines by adjusting slope weight (w) and baseline intercept (b)."
            },
            {
                "title": "Measuring Mistakes: Mean Squared Error (MSE)",
                "content_markdown": "To measure how well our line fits the data, we calculate the **Mean Squared Error (MSE)**:\n1. Find the gap (residual) between the predicted value and true value: $(\\hat{y} - y)$.\n2. Square the gap so negative errors don't cancel positive errors: $(\\hat{y} - y)^2$.\n3. Take the average across all training data points:\n\n$$MSE = \\frac{1}{N} \\sum_{i=1}^N (y_{pred}^{(i)} - y_{true}^{(i)})^2$$\n\nA lower MSE score means our line makes much more accurate predictions.",
                "key_takeaway": "Squaring the errors heavily penalizes large mistakes, pushing the model to fit all points evenly."
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
            "title": "Training Linear Regression with Gradient Descent in NumPy",
            "language": "python",
            "code": "import numpy as np\n\n# Sample dataset: House size (X) and Price (y)\n# True relationship: Price = 2.5 * Size + 4.0 + random noise\nnp.random.seed(42)\nX = np.array([[1.0], [2.0], [3.0], [4.0]])\ny = np.array([[6.5], [9.0], [11.5], [14.0]])\n\n# Initialize model starting parameters\nw = 0.0\nb = 0.0\nlearning_rate = 0.05\nepochs = 100\nN = len(X)\n\nfor epoch in range(epochs):\n    # 1. Make predictions\n    y_pred = w * X + b\n    # 2. Compute error gradients\n    dw = (2 / N) * np.sum((y_pred - y) * X)\n    db = (2 / N) * np.sum(y_pred - y)\n    # 3. Update parameters downhill\n    w -= learning_rate * dw\n    b -= learning_rate * db\n\nprint(f\"Learned Weight (w): {w:.2f} (Target: ~2.50)\")\nprint(f\"Learned Bias (b):   {b:.2f} (Target: ~4.00)\")",
            "explanation": "Illustrates the complete optimization loop of Gradient Descent tuning weight w and bias b to fit the points.",
            "output_preview": "Learned Weight (w): 2.47 (Target: ~2.50)\nLearned Bias (b):   4.08 (Target: ~4.00)"
        },
        "quiz_id": "quiz-ml-linear-regression-ols",
        "summary": "You learned how linear regression fits lines to data points and minimizes Mean Squared Error.",
        "next_lesson_slug": "dl-perceptron-forward-prop",
        "prev_lesson_slug": "math-derivatives-gradients"
    },
    # Lesson 6: Deep Learning
    {
        "slug": "dl-perceptron-forward-prop",
        "course_slug": "deep-learning-fundamentals",
        "module_id": "dl-mod-1",
        "title": "Artificial Neurons, Layers & Activation Functions",
        "order": 1,
        "estimated_minutes": 25,
        "difficulty": "Intermediate",
        "skill_tag": "neural_networks",
        "learning_objectives": [
            "Learn how an artificial neuron combines inputs with weights and bias.",
            "Understand why non-linear activation functions (ReLU, Sigmoid) are essential.",
            "See how stacking layers allows networks to recognize complex shapes and patterns."
        ],
        "theory_sections": [
            {
                "title": "How a Single Neuron Thinks",
                "content_markdown": "An **artificial neuron** is inspired by biological brain cells:\n1. It takes in multiple input numbers ($x_1, x_2, \\dots$).\n2. Multiplies each input by an importance weight ($w_1, w_2, \\dots$).\n3. Adds a base threshold bias ($b$).\n4. Passes the result through an **activation function** $\\sigma(z)$ to decide how strongly to fire:\n\n$$z = (w_1 x_1 + w_2 x_2 + ... + w_n x_n) + b$$\n$$\\text{Output } a = \\sigma(z)$$",
                "key_takeaway": "Each neuron acts as a specialized pattern detector."
            },
            {
                "title": "Why Do We Need Activation Functions?",
                "content_markdown": "If we only did addition and multiplication, stacking 100 neural layers would still just equal one giant straight line!\n\n**Activation functions (like ReLU or Sigmoid)** introduce curves and bends. For example, **ReLU** (Rectified Linear Unit) has a simple rule:\n\n$$\\text{ReLU}(z) = \\max(0, z)$$\n\nIf the input $z$ is negative, output `0`. If positive, output $z$. This simple on/off switch enables deep networks to bend decision boundaries around complex shapes like circles, faces, and speech patterns.",
                "key_takeaway": "Activation functions bend the math, allowing networks to learn complex non-linear patterns."
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
            "title": "Building a 2-Layer Neural Network Forward Pass in NumPy",
            "language": "python",
            "code": "import numpy as np\n\ndef relu(z):\n    \"\"\"Zero out negative values, keep positive values unchanged.\"\"\"\n    return np.maximum(0, z)\n\n# 2 input samples with 3 features each\nX = np.array([\n    [1.0, 2.0, -1.0],\n    [0.5, -1.5, 2.0]\n])\n\n# Layer 1 weights: 3 inputs -> 4 hidden neurons\nW1 = np.random.randn(3, 4) * 0.1\nb1 = np.zeros((1, 4))\n\n# Forward pass through Layer 1\nZ1 = np.dot(X, W1) + b1\nA1 = relu(Z1)  # Apply ReLU activation\n\nprint(\"Input batch shape:\", X.shape)\nprint(\"Hidden layer activation shape:\", A1.shape)\nprint(\"Sample 0 activations:\\n\", np.round(A1[0], 3))",
            "explanation": "Demonstrates matrix multiplication followed by non-linear ReLU activation for a hidden layer.",
            "output_preview": "Input batch shape: (2, 3)\nHidden layer activation shape: (2, 4)\nSample 0 activations:\n [0.082 0.    0.145 0.   ]"
        },
        "quiz_id": "quiz-dl-perceptron-forward-prop",
        "summary": "You explored artificial neurons, why non-linear activations are necessary, and how layers pass signals forward.",
        "next_lesson_slug": "genai-self-attention-transformers",
        "prev_lesson_slug": "ml-linear-regression-ols"
    },
    # Lesson 7: GenAI
    {
        "slug": "genai-self-attention-transformers",
        "course_slug": "generative-ai-fundamentals",
        "module_id": "genai-mod-2",
        "title": "The Self-Attention Mechanism Behind ChatGPT",
        "order": 1,
        "estimated_minutes": 30,
        "difficulty": "Advanced",
        "skill_tag": "transformers",
        "learning_objectives": [
            "Learn how Self-Attention allows words to look at surrounding words for context.",
            "Understand Query ($Q$), Key ($K$), and Value ($V$) with the filing cabinet analogy.",
            "Understand the Attention formula: Softmax(QKᵀ / √d_k) · V."
        ],
        "theory_sections": [
            {
                "title": "Why Does Attention Matter?",
                "content_markdown": "In human language, the meaning of a word depends entirely on the words around it.\n\nConsider the sentence:\n> *'The bank on the river was muddy.'* vs *'The bank approved my loan.'*\n\nWithout attention, the word *'bank'* would have the exact same representation. **Self-Attention acts like a dynamic mental spotlight** that connects *'bank'* to *'river'* in the first sentence and *'bank'* to *'loan'* in the second sentence!",
                "key_takeaway": "Self-attention lets words update their meaning based on all other words in the sentence simultaneously."
            },
            {
                "title": "The Query, Key, and Value Analogy",
                "content_markdown": "To compute attention, every word is projected into 3 vectors, just like searching a library or YouTube:\n1. **Query ($Q$)**: *What am I searching for?* (e.g. *'Who does pronoun \"it\" refer to?'*)\n2. **Key ($K$)**: *The title tag / label on each file in the library.* (e.g. *'animal'*, *'street'*)\n3. **Value ($V$)**: *The actual content inside the matched file.*\n\n$$\\text{Attention}(Q, K, V) = \\text{Softmax}\\left( \\frac{Q · K^T}{\\sqrt{d_k}} \\right) · V$$\n\n1. Multiply $Q$ and $K^T$ to score how relevant each word is to every other word.\n2. Divide by $\\sqrt{d_k}$ to prevent numbers from blowing up.\n3. Pass scores through `Softmax` so all attention weights sum up to 100% (`1.0`).\n4. Multiply by $V$ to get the final context-aware word representation.",
                "key_takeaway": "The Attention equation simply calculates a weighted average of word contents based on relevance scores."
            }
        ],
        "visual_explainer": {
            "type": "diagram",
            "title": "Scaled Dot-Product Attention Flow",
            "subtitle": "Q * K^T -> Scale -> Softmax -> Weight Values (V)",
            "diagram_type": "attention_matrix"
        },
        "code_example": {
            "title": "Computing Self-Attention in Pure NumPy",
            "language": "python",
            "code": "import numpy as np\n\ndef softmax(x):\n    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))\n    return e_x / np.sum(e_x, axis=-1, keepdims=True)\n\ndef self_attention(Q, K, V):\n    d_k = Q.shape[-1]\n    # 1. Similarity scores between queries and keys\n    scores = np.matmul(Q, K.T) / np.sqrt(d_k)\n    # 2. Convert to probabilities summing to 1.0\n    weights = softmax(scores)\n    # 3. Weighted blend of values\n    output = np.matmul(weights, V)\n    return output, weights\n\n# 3 Tokens: ['AI', 'is', 'awesome'], feature dim = 4\nnp.random.seed(42)\nQ = np.random.randn(3, 4)\nK = np.random.randn(3, 4)\nV = np.random.randn(3, 4)\n\ncontext_output, attention_matrix = self_attention(Q, K, V)\nprint(\"Attention Weights Matrix (3x3):\\n\", np.round(attention_matrix, 3))\nprint(\"Row 0 attention sum check:\", np.sum(attention_matrix[0]))",
            "explanation": "Computes attention scores and verifies that every row of the attention matrix sums to 1.0 (100% attention distribution).",
            "output_preview": "Attention Weights Matrix (3x3):\n [[0.219 0.443 0.338]\n  [0.495 0.384 0.121]\n  [0.428 0.301 0.271]]\nRow 0 attention sum check: 1.0"
        },
        "quiz_id": "quiz-genai-self-attention-transformers",
        "summary": "You mastered Query/Key/Value dynamics, attention matrix weighting, and how Transformers contextualize language.",
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
                "question": "In Python, numbers (integers, floats) and strings are immutable (cannot be altered in-place).",
                "options": ["True", "False"],
                "correct_answer": 0,
                "points": 10,
                "skill_tag": "python_basics",
                "explanation": "True. Numeric types (int, float) and strings are immutable. Any modification (like `x += 1`) creates a brand new number object rather than modifying the existing memory block in-place."
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
        "title": "Vectors & Dot Products Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "If two non-zero vectors u and v have a dot product u · v = 0, what does this indicate geometrically?",
                "options": [
                    "They point in exactly the same direction",
                    "They are orthogonal (perpendicular / 90 degrees apart with 0 similarity)",
                    "One of the vectors has length zero",
                    "They point in opposite directions (180 degrees)"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "linear_algebra",
                "explanation": "When the dot product between two non-zero vectors is 0, cos(theta) = 0, meaning the angle between them is 90 degrees (completely independent / orthogonal).",
                "hint": "Recall that a dot product of 0 means 90 degree angle."
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
                "question": "In Gradient Descent optimization, in which direction do we update model weights to reduce prediction error?",
                "options": [
                    "In the direction of the gradient (+∇L) to go uphill",
                    "In the opposite direction of the gradient (-∇L) to go downhill toward lowest error",
                    "At a random 90-degree angle to the gradient",
                    "Weights are never updated using the gradient"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "calculus",
                "explanation": "The gradient vector points in the direction of steepest increase (uphill). Therefore, taking steps in the negative gradient direction (-∇L) takes us downhill toward minimum loss.",
                "hint": "We want to decrease error, so we move opposite to the steepest uphill direction."
            }
        ]
    },
    {
        "id": "quiz-ml-linear-regression-ols",
        "lesson_slug": "ml-linear-regression-ols",
        "title": "Linear Regression & Loss Functions Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "In the linear regression equation y_hat = w · x + b, what does parameter b represent?",
                "options": [
                    "The slope (rate of change per unit of x)",
                    "The bias / y-intercept (the baseline prediction when input feature x is 0)",
                    "The total number of training rows",
                    "The learning rate"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "regression",
                "explanation": "Parameter b is the bias (or intercept). It shifts the line up or down so the model can make predictions when all input features x are zero.",
                "hint": "Think of y = mx + b where b is the y-intercept."
            }
        ]
    },
    {
        "id": "quiz-dl-perceptron-forward-prop",
        "lesson_slug": "dl-perceptron-forward-prop",
        "title": "Artificial Neurons & Activations Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "What is the primary mathematical reason for using non-linear activation functions (like ReLU) in deep neural networks?",
                "options": [
                    "To speed up matrix multiplication hardware",
                    "To prevent multiple linear layers from collapsing into a single simple linear model, enabling complex pattern recognition",
                    "To convert all numbers to integers",
                    "To eliminate all negative numbers from the computer's memory"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "neural_networks",
                "explanation": "Without non-linear activations, stacking 100 neural layers is mathematically equivalent to a single linear layer (W2 * W1 * x = W_combined * x). Non-linear activations allow networks to learn curved, complex boundaries.",
                "hint": "Without non-linearities, linear layers simply multiply into another straight line."
            }
        ]
    },
    {
        "id": "quiz-genai-self-attention-transformers",
        "lesson_slug": "genai-self-attention-transformers",
        "title": "Self-Attention & Transformers Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "In the Transformer attention equation Softmax(Q·Kᵀ / √d_k) · V, why do we divide the dot products by √d_k?",
                "options": [
                    "To convert the matrix into text characters",
                    "To scale dot product magnitudes and prevent vanishing gradients during Softmax backpropagation",
                    "To remove punctuation marks from sentences",
                    "To calculate the total number of words in the vocabulary"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "transformers",
                "explanation": "In high dimensions d_k, dot products grow large in magnitude, which would push the Softmax function into flat regions with tiny gradients. Dividing by √d_k stabilizes variance to 1.0.",
                "hint": "Dividing by √d_k keeps numbers within a well-behaved range for Softmax."
            }
        ]
    }
]

SKILLS_DATA = [
    {
        "id": "skill-python-basics",
        "name": "Python & NumPy Computing",
        "category": "Programming",
        "description": "Object reference models, mutability, vectorization, and broadcasting.",
        "icon": "Code2",
        "tier": 1,
        "prerequisites": [],
        "mastery_threshold": 70,
        "matching_lessons": ["py-intro-variables", "py-numpy-arrays-broadcasting"]
    },
    {
        "id": "skill-linear-algebra",
        "name": "Linear Algebra & Vectors",
        "category": "Mathematics",
        "description": "Vector dot products, geometric cosine similarity, and matrix projections.",
        "icon": "Binary",
        "tier": 1,
        "prerequisites": ["skill-python-basics"],
        "mastery_threshold": 70,
        "matching_lessons": ["math-vectors-dot-products"]
    },
    {
        "id": "skill-calculus",
        "name": "Calculus & Optimization",
        "category": "Mathematics",
        "description": "Derivatives, partial slopes, and gradient vector descent paths.",
        "icon": "TrendingUp",
        "tier": 2,
        "prerequisites": ["skill-linear-algebra"],
        "mastery_threshold": 70,
        "matching_lessons": ["math-derivatives-gradients"]
    },
    {
        "id": "skill-regression",
        "name": "Classical Machine Learning",
        "category": "Machine Learning",
        "description": "Linear regression, loss surfaces, and MSE optimization.",
        "icon": "Cpu",
        "tier": 2,
        "prerequisites": ["skill-calculus"],
        "mastery_threshold": 70,
        "matching_lessons": ["ml-linear-regression-ols"]
    },
    {
        "id": "skill-neural-networks",
        "name": "Deep Neural Networks",
        "category": "Deep Learning",
        "description": "Multi-layer perceptron forward propagation and non-linear activations.",
        "icon": "Network",
        "tier": 3,
        "prerequisites": ["skill-regression"],
        "mastery_threshold": 70,
        "matching_lessons": ["dl-perceptron-forward-prop"]
    },
    {
        "id": "skill-transformers",
        "name": "Transformers & Generative AI",
        "category": "Generative AI",
        "description": "Query/Key/Value self-attention, token contextualization, and scaling.",
        "icon": "Sparkles",
        "tier": 4,
        "prerequisites": ["skill-neural-networks"],
        "mastery_threshold": 70,
        "matching_lessons": ["genai-self-attention-transformers"]
    }
]
