"""Comprehensive curriculum seed data for AI Learning Lab.
All courses and lessons are designed to be intuitive, highly visual, 
and explained in simple, beginner-friendly terms with practical analogies.
"""

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
        "syllabus_overview": "This course builds the foundational programming skills necessary for every modern AI engineer. We move from core Python concepts to fast vectorized math in NumPy and structured tabular data manipulation in Pandas.",
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
        "syllabus_overview": "Deep learning allows computers to recognize images, translate languages, and beat grandmasters. Learn how networks build representations layer by layer.",
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
    },
    {
        "slug": "prompt-engineering-agents",
        "title": "Prompt Engineering & AI Autonomous Agents",
        "description": "Crafting high-precision prompts, multi-step chain of thought reasoning, and building AI agents that use external APIs and tools.",
        "category": "Practical AI",
        "level": "Beginner",
        "estimated_hours": 10,
        "icon": "Bot",
        "color": "#F59E0B",
        "order": 6,
        "is_published": True,
        "prerequisites": ["python-foundations"],
        "skills_taught": ["System Prompts", "Few-Shot Prompting", "Chain of Thought", "Tool Calling & ReAct", "Autonomous Agents"],
        "syllabus_overview": "Learn how to steer foundation models with precision. From structured output schemas and reasoning frameworks to building interactive ReAct agents that browse databases and execute code.",
        "modules": [
            {
                "id": "agent-mod-1",
                "title": "Module 1: Prompt Engineering Foundations",
                "description": "System instructions, structured output formatting, delimiters, and few-shot examples.",
                "order": 1,
                "lesson_ids": ["prompt-foundations-few-shot"]
            },
            {
                "id": "agent-mod-2",
                "title": "Module 2: Advanced Reasoning & Chain of Thought",
                "description": "Unlocking complex logical deductions with Chain-of-Thought and self-consistency.",
                "order": 2,
                "lesson_ids": ["prompt-chain-of-thought-reasoning"]
            },
            {
                "id": "agent-mod-3",
                "title": "Module 3: Building Autonomous AI Agents",
                "description": "Function calling, external tool usage, and the ReAct (Reason + Act) loop.",
                "order": 3,
                "lesson_ids": ["prompt-ai-agents-tool-use"]
            }
        ]
    }
]

LESSONS_DATA = [
    # =========================================================================
    # COURSE 1: PYTHON & NUMPY FOUNDATIONS
    # =========================================================================
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
        "next_lesson_slug": "py-data-structures-comprehensions",
        "prev_lesson_slug": None
    },
    {
        "slug": "py-data-structures-comprehensions",
        "course_slug": "python-foundations",
        "module_id": "py-mod-1",
        "title": "Lists, Dictionaries & Supercharged List Comprehensions",
        "order": 2,
        "estimated_minutes": 15,
        "difficulty": "Beginner",
        "skill_tag": "python_basics",
        "learning_objectives": [
            "Master Python dictionaries for feature storage and metadata mapping.",
            "Use list and dictionary comprehensions to transform data in a single clean line.",
            "Filter outliers and normalize data with clean Pythonic expressions."
        ],
        "theory_sections": [
            {
                "title": "Dictionaries: The Backbone of AI Datasets",
                "content_markdown": "In Machine Learning, almost every sample is a key-value dictionary (e.g., `{\"age\": 25, \"income\": 50000, \"label\": 1}`).\n\nDictionaries give **instant O(1) lookup time** by hash key, making them ideal for storing vocabularies, token mappings, and model configurations.",
                "key_takeaway": "Use dictionaries for fast feature lookups and category-to-number mappings."
            },
            {
                "title": "List Comprehensions: Fast & Readable Transformations",
                "content_markdown": "Instead of writing 4-line `for` loops to process numbers:\n\n```python\n# Slow & bulky:\nscaled = []\nfor x in raw_data:\n    if x > 0:\n        scaled.append(x * 2)\n\n# Pythonic 1-liner:\nscaled = [x * 2 for x in raw_data if x > 0]\n```\n\nList comprehensions run in compiled C speed under the hood in Python, making them faster and much easier to read.",
                "key_takeaway": "List comprehensions combine transformation and filtering into one concise, fast statement."
            }
        ],
        "visual_explainer": {
            "type": "diagram",
            "title": "List Comprehension Pipeline",
            "subtitle": "Input List -> Filter Condition -> Expression Transform -> Output List",
            "diagram_type": "data_pipeline",
            "parameters": {"input_size": 5, "filtered_size": 3}
        },
        "code_example": {
            "title": "Building a Token-to-ID Vocabulary with Dict Comprehensions",
            "language": "python",
            "code": "# Unique words in our AI dataset\nvocab = ['<PAD>', 'apple', 'banana', 'cherry', '<UNK>']\n\n# Build mapping: word -> integer ID\nword2id = {word: idx for idx, word in enumerate(vocab)}\n\n# Build reverse mapping: integer ID -> word\nid2word = {idx: word for word, idx in word2id.items()}\n\nprint(\"Word to ID mapping:\", word2id)\nprint(\"Looking up ID for 'banana':\", word2id['banana'])\nprint(\"Reversing ID 2 back to word:\", id2word[2])",
            "explanation": "Demonstrates dictionary comprehensions to build the bidirectional vocabulary lookup tables used in every NLP model.",
            "output_preview": "Word to ID mapping: {'<PAD>': 0, 'apple': 1, 'banana': 2, 'cherry': 3, '<UNK>': 4}\nLooking up ID for 'banana': 2\nReversing ID 2 back to word: banana"
        },
        "quiz_id": "quiz-py-data-structures-comprehensions",
        "summary": "You mastered dictionaries and list comprehensions to cleanly transform and filter data.",
        "next_lesson_slug": "py-numpy-arrays-broadcasting",
        "prev_lesson_slug": "py-intro-variables"
    },
    {
        "slug": "py-numpy-arrays-broadcasting",
        "course_slug": "python-foundations",
        "module_id": "py-mod-2",
        "title": "NumPy Arrays & Fast Broadcasting",
        "order": 3,
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
                "content_markdown": "Standard Python lists are flexible but slow because each number is wrapped in a full Python object stored across scattered memory addresses.\n\n**NumPy arrays (`ndarray`) pack numbers side-by-side in raw computer memory**, like books lined up neatly on a bookshelf. This allows your processor to calculate thousands of numbers in a single clock cycle (SIMD vectorization), making matrix math **50x to 200x faster** than a Python `for` loop.",
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
        "next_lesson_slug": "py-numpy-matrix-operations",
        "prev_lesson_slug": "py-data-structures-comprehensions"
    },
    {
        "slug": "py-numpy-matrix-operations",
        "course_slug": "python-foundations",
        "module_id": "py-mod-2",
        "title": "Matrix Multiplication, Dot Products & Reshaping",
        "order": 4,
        "estimated_minutes": 20,
        "difficulty": "Beginner",
        "skill_tag": "numpy_basics",
        "learning_objectives": [
            "Differentiate element-wise multiplication (*) from matrix multiplication (@ or np.dot).",
            "Master matrix reshaping and flattening (turning 2D images into 1D vectors).",
            "Understand the inner-dimension matching rule: (M, K) @ (K, N) -> (M, N)."
        ],
        "theory_sections": [
            {
                "title": "Element-Wise (*) vs Matrix Multiplication (@)",
                "content_markdown": "One of the most common beginner bugs in machine learning is mixing up `*` and `@`:\n\n* **`A * B` (Element-wise / Hadamard)**: Multiplies matching slots individually. Both matrices must have matching shapes.\n* **`A @ B` (Matrix Multiplication)**: Takes rows of A and computes dot products with columns of B. **The columns of A must match the rows of B!**",
                "key_takeaway": "In neural networks, passing data through a layer is always matrix multiplication: output = inputs @ weights + bias."
            },
            {
                "title": "Reshaping Tensors",
                "content_markdown": "In computer vision, a grayscale image is a 28x28 grid of pixels (784 numbers). To feed it into a linear classifier, we **reshape** or **flatten** it into a single vector of shape `(784,)` or `(1, 784)`.\n\nUsing `array.reshape(rows, -1)` lets NumPy automatically calculate the missing dimension.",
                "key_takeaway": "Reshaping reorganizes dimensions without moving or duplicating the underlying data in memory."
            }
        ],
        "visual_explainer": {
            "type": "diagram",
            "title": "Matrix Multiplication Shape Rule",
            "subtitle": "(Batch Size, Features) @ (Features, Hidden) -> (Batch Size, Hidden)",
            "diagram_type": "matrix_dimension_match",
            "parameters": {"shape_A": [4, 3], "shape_B": [3, 2], "shape_out": [4, 2]}
        },
        "code_example": {
            "title": "Matrix Operations and Neural Layer Simulation",
            "language": "python",
            "code": "import numpy as np\n\n# 2 input samples (e.g. 2 user profiles with 3 features each)\nX = np.array([\n    [1.0, 2.0, 3.0],\n    [0.5, 1.5, 2.5]\n])\n\n# Layer weights: 3 input features -> 2 output predictions\nW = np.array([\n    [0.2, 0.8],\n    [0.5, 0.1],\n    [-0.3, 0.4]\n])\nb = np.array([0.1, -0.2])\n\n# Calculate layer output: Y = X @ W + b\nY = X @ W + b\n\nprint(\"Input shape:\", X.shape)\nprint(\"Weights shape:\", W.shape)\nprint(\"Layer Output shape:\", Y.shape)\nprint(\"Layer Output values:\\n\", np.round(Y, 3))",
            "explanation": "Calculates the forward pass of a basic linear layer with 2 samples passing through 2 output neurons.",
            "output_preview": "Input shape: (2, 3)\nWeights shape: (3, 2)\nLayer Output shape: (2, 2)\nLayer Output values:\n [[ 0.4   2.  ]\n  [ 0.2   1.35]]"
        },
        "quiz_id": "quiz-py-numpy-matrix-operations",
        "summary": "You learned the crucial difference between element-wise math and matrix multiplication, and how to reshape tensors.",
        "next_lesson_slug": "py-pandas-dataframes-cleaning",
        "prev_lesson_slug": "py-numpy-arrays-broadcasting"
    },
    {
        "slug": "py-pandas-dataframes-cleaning",
        "course_slug": "python-foundations",
        "module_id": "py-mod-3",
        "title": "Pandas: Loading, Filtering & Cleaning Messy AI Data",
        "order": 5,
        "estimated_minutes": 20,
        "difficulty": "Beginner",
        "skill_tag": "data_preprocessing",
        "learning_objectives": [
            "Understand DataFrames as organized tables with named columns and row indices.",
            "Filter, sort, and select data slices using boolean conditions and `.loc`/`.iloc`.",
            "Impute missing values (`NaN`) and convert categorical text to numerical labels."
        ],
        "theory_sections": [
            {
                "title": "Data Is Always Messy",
                "content_markdown": "Real-world AI projects spend 80% of their time preparing data. Real datasets contain:\n* Missing values (`NaN` or `None`)\n* Inconsistent text ('Yes', 'yes', 'Y')\n* Outliers and corrupted rows\n\n**Pandas** provides fast, tabular tools built on top of NumPy to clean and structure data before sending it to machine learning models.",
                "key_takeaway": "Clean data produces reliable models. Garbage in means garbage out."
            },
            {
                "title": "Handling Missing Values",
                "content_markdown": "Machine learning algorithms crash if given `NaN` (Not a Number). You have two main strategies:\n1. **Drop rows (`df.dropna()`)**: Good if only 1% of rows are missing.\n2. **Impute (`df.fillna(df.mean())`)**: Replace missing numbers with column mean/median to retain all data rows.",
                "key_takeaway": "Always inspect and fill missing values before converting a DataFrame to a NumPy training matrix."
            }
        ],
        "visual_explainer": {
            "type": "table_preview",
            "title": "DataFrame Cleaning Pipeline",
            "subtitle": "Raw CSV -> Impute Missing Values -> Encode Labels -> ML Matrix (X, y)",
            "diagram_type": "tabular_pipeline"
        },
        "code_example": {
            "title": "Loading, Cleaning & Preparing a Dataset in Pandas",
            "language": "python",
            "code": "import pandas as pd\nimport numpy as np\n\n# Simulated raw tabular data\nraw_data = {\n    'Age': [22, 38, np.nan, 35, 54],\n    'Salary': [45000, 82000, 61000, np.nan, 110000],\n    'Purchased': ['No', 'Yes', 'No', 'Yes', 'Yes']\n}\n\ndf = pd.DataFrame(raw_data)\nprint(\"--- Raw Dataset ---\")\nprint(df)\n\n# 1. Fill missing numeric values with column median\ndf['Age'] = df['Age'].fillna(df['Age'].median())\ndf['Salary'] = df['Salary'].fillna(df['Salary'].median())\n\n# 2. Convert 'Purchased' text into binary 0/1 integers\ndf['Purchased'] = df['Purchased'].map({'No': 0, 'Yes': 1})\n\nprint(\"\\n--- Cleaned ML-Ready Dataset ---\")\nprint(df)",
            "explanation": "Demonstrates replacing missing values with median statistics and mapping text categories into numbers.",
            "output_preview": "--- Raw Dataset ---\n    Age    Salary Purchased\n0  22.0   45000.0        No\n1  38.0   82000.0       Yes\n2   NaN   61000.0        No\n3  35.0       NaN       Yes\n4  54.0  110000.0       Yes\n\n--- Cleaned ML-Ready Dataset ---\n    Age    Salary  Purchased\n0  22.0   45000.0          0\n1  38.0   82000.0          1\n2  36.5   61000.0          0\n3  35.0   71500.0          1\n4  54.0  110000.0          1"
        },
        "quiz_id": "quiz-py-pandas-dataframes-cleaning",
        "summary": "You learned how to clean tabular datasets, fill missing values, and prepare data for ML models.",
        "next_lesson_slug": "math-vectors-dot-products",
        "prev_lesson_slug": "py-numpy-matrix-operations"
    },

    # =========================================================================
    # COURSE 2: MATHEMATICS FOR ARTIFICIAL INTELLIGENCE
    # =========================================================================
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
        "next_lesson_slug": "math-matrix-multiplication",
        "prev_lesson_slug": "py-pandas-dataframes-cleaning"
    },
    {
        "slug": "math-matrix-multiplication",
        "course_slug": "math-for-ai",
        "module_id": "math-mod-1",
        "title": "Matrix Multiplication: Geometric Transformations Made Easy",
        "order": 2,
        "estimated_minutes": 20,
        "difficulty": "Intermediate",
        "skill_tag": "linear_algebra",
        "learning_objectives": [
            "Visualize matrices as geometric transformations that stretch, rotate, and project space.",
            "Understand how multiplying a dataset matrix by a weight matrix transforms raw features into predictions.",
            "Grasp why GPUs excel at parallel matrix multiplication."
        ],
        "theory_sections": [
            {
                "title": "Matrices as Space Modifiers",
                "content_markdown": "Instead of viewing a matrix as a boring spreadsheet of numbers, think of it as a **space transformer**:\n* It can rotate 2D points by 45 degrees.\n* It can stretch space horizontally or compress it vertically.\n* It can project a 1000-dimensional image down into a compact 10-dimensional summary!\n\nWhen you multiply an input vector $x$ by a weight matrix $W$, you are transforming your data into a new coordinate system where patterns are easier to separate.",
                "key_takeaway": "Matrix multiplication rotates and warps data space to make classifications clear."
            },
            {
                "title": "Why Neural Networks Rely on Matrices",
                "content_markdown": "A neural network layer with 1,000 inputs and 500 outputs needs 500,000 individual weight connections.\n\nInstead of computing 500,000 separate equations one by one, we write:\n$$Y = X · W + b$$\n\nModern GPUs contain thousands of tiny tensor cores designed specifically to execute these matrix operations simultaneously in nanoseconds.",
                "key_takeaway": "Matrix formulation allows parallel hardware (GPUs/TPUs) to compute millions of predictions simultaneously."
            }
        ],
        "visual_explainer": {
            "type": "diagram",
            "title": "2D Space Rotation via Transformation Matrix",
            "subtitle": "Grid lines warping under 2x2 linear transformation",
            "diagram_type": "space_transformation",
            "parameters": {"angle_deg": 45, "scale_x": 1.2, "scale_y": 0.8}
        },
        "code_example": {
            "title": "Rotating 2D Geometric Points with a Rotation Matrix",
            "language": "python",
            "code": "import numpy as np\n\n# Square coordinates in 2D space: [x, y]\nsquare = np.array([\n    [1.0, 1.0],\n    [-1.0, 1.0],\n    [-1.0, -1.0],\n    [1.0, -1.0]\n])\n\n# 90-degree counterclockwise rotation matrix\ntheta = np.radians(90)\nrotation_matrix = np.array([\n    [np.cos(theta), -np.sin(theta)],\n    [np.sin(theta),  np.cos(theta)]\n])\n\n# Rotate all points at once: (N, 2) @ (2, 2)\nrotated_square = square @ rotation_matrix.T\n\nprint(\"Original Point [1, 1] rotated to:\", np.round(rotated_square[0], 2))\nprint(\"Original Point [-1, 1] rotated to:\", np.round(rotated_square[1], 2))",
            "explanation": "Applies a 90-degree 2D rotation matrix across multiple coordinate vertices in a single matrix multiplication step.",
            "output_preview": "Original Point [1, 1] rotated to: [-1.  1.]\nOriginal Point [-1, 1] rotated to: [-1. -1.]"
        },
        "quiz_id": "quiz-math-matrix-multiplication",
        "summary": "You visualized matrix multiplication as geometric transformations and learned why it powers deep learning on GPUs.",
        "next_lesson_slug": "math-derivatives-gradients",
        "prev_lesson_slug": "math-vectors-dot-products"
    },
    {
        "slug": "math-derivatives-gradients",
        "course_slug": "math-for-ai",
        "module_id": "math-mod-2",
        "title": "Derivatives, Slopes & The Gradient Compass",
        "order": 3,
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
        "next_lesson_slug": "math-chain-rule-backprop-math",
        "prev_lesson_slug": "math-matrix-multiplication"
    },
    {
        "slug": "math-chain-rule-backprop-math",
        "course_slug": "math-for-ai",
        "module_id": "math-mod-2",
        "title": "The Chain Rule: Passing Slopes Through Connected Equations",
        "order": 4,
        "estimated_minutes": 25,
        "difficulty": "Intermediate",
        "skill_tag": "calculus",
        "learning_objectives": [
            "Understand the Chain Rule as multiplying rates of change along a chain of gears or dominoes.",
            "See how changing an early weight propagates through intermediate layers to change the final loss.",
            "Master the core mathematical foundation behind Backpropagation."
        ],
        "theory_sections": [
            {
                "title": "The Gear Analogy",
                "content_markdown": "Imagine three connected gears: A, B, and C.\n* When Gear A turns 1 time, Gear B turns 2 times ($\\frac{dB}{dA} = 2$).\n* When Gear B turns 1 time, Gear C turns 3 times ($\\frac{dC}{dB} = 3$).\n\nHow many times does Gear C turn when you turn Gear A once? **You multiply them!**\n$$\\frac{dC}{dA} = \\frac{dC}{dB} × \\frac{dB}{dA} = 3 × 2 = 6$$\n\nThat is the **Chain Rule**! If functions are nested $y = f(g(x))$, you simply multiply their local derivatives together.",
                "key_takeaway": "The Chain Rule lets you find how a change at the beginning of a long network affects the final output by multiplying local slopes."
            },
            {
                "title": "Why AI Needs the Chain Rule",
                "content_markdown": "In a 50-layer deep neural network, the loss at the end depends on Layer 50, which depends on Layer 49... all the way back to Layer 1.\n\nThe Chain Rule allows us to compute the exact gradient for Layer 1 by smoothly multiplying backwards step-by-step.",
                "key_takeaway": "Backpropagation is simply the Chain Rule implemented efficiently from right to left."
            }
        ],
        "visual_explainer": {
            "type": "diagram",
            "title": "Chain Rule Derivative Flow",
            "subtitle": "dL/dw = (dL/dy) * (dy/dz) * (dz/dw)",
            "diagram_type": "computational_graph",
            "parameters": {"nodes": ["w", "z = w*x", "y = relu(z)", "Loss = (y-t)^2"]}
        },
        "code_example": {
            "title": "Manual Chain Rule Computation vs Numerical Derivative",
            "language": "python",
            "code": "# Function: y = (2x + 1)^2\n# Local functions: u = 2x + 1, y = u^2\nx = 3.0\n\n# Forward pass\nu = 2 * x + 1    # u = 7.0\ny = u ** 2       # y = 49.0\n\n# Analytical Chain Rule: dy/dx = (dy/du) * (du/dx)\ndy_du = 2 * u    # dy/du = 14.0\ndu_dx = 2.0      # du/dx = 2.0\ndy_dx = dy_du * du_dx  # 14.0 * 2.0 = 28.0\n\n# Numerical check: [f(x+h) - f(x)] / h\nh = 0.0001\nnumerical_dy_dx = (((2 * (x + h) + 1)**2) - y) / h\n\nprint(f\"Analytical Chain Rule Gradient: {dy_dx:.4f}\")\nprint(f\"Numerical Approximation:       {numerical_dy_dx:.4f}\")",
            "explanation": "Calculates the derivative of a composite function using the chain rule and verifies it against finite differences.",
            "output_preview": "Analytical Chain Rule Gradient: 28.0000\nNumerical Approximation:       28.0004"
        },
        "quiz_id": "quiz-math-chain-rule-backprop-math",
        "summary": "You understood the Chain Rule as gear multiplication and learned how gradients flow backwards through connected layers.",
        "next_lesson_slug": "math-probability-bayes-theorem",
        "prev_lesson_slug": "math-derivatives-gradients"
    },
    {
        "slug": "math-probability-bayes-theorem",
        "course_slug": "math-for-ai",
        "module_id": "math-mod-3",
        "title": "Probability & Bayes' Theorem: Updating Beliefs with Evidence",
        "order": 5,
        "estimated_minutes": 20,
        "difficulty": "Intermediate",
        "skill_tag": "probability",
        "learning_objectives": [
            "Differentiate Prior Probability (base belief) from Posterior Probability (updated belief).",
            "Understand Bayes' Theorem formula and its application in spam filtering and medical diagnostics.",
            "Learn how Naive Bayes classifiers make rapid text predictions."
        ],
        "theory_sections": [
            {
                "title": "Updating Beliefs with Evidence",
                "content_markdown": "In life and machine learning, you start with a **prior belief** before seeing any evidence.\n\n* *Prior*: Only 1% of emails in your inbox are malicious phishing attacks.\n* *New Evidence*: An incoming email contains the phrase *'CLAIM YOUR $1,000,000 PRIZE IMMEDIATELY'*\n* *Posterior (Updated Belief)*: Given this strong evidence, the probability this email is phishing jumps from 1% to 99.8%!\n\n**Bayes' Theorem** gives the exact mathematical formula to update our belief:\n$$P(A|B) = \\frac{P(B|A) · P(A)}{P(B)}$$",
                "key_takeaway": "Bayes' Theorem tells us how to rationally update our predictions as new clues arrive."
            },
            {
                "title": "Why 'Naive' Bayes Is So Powerful",
                "content_markdown": "Naive Bayes assumes all word clues are independent of each other (e.g., seeing *'lottery'* and *'free'* are evaluated as separate independent multipliers).\n\nEven though words aren't completely independent in real grammar, this simplification runs in microseconds and remains one of the fastest, most effective baseline classifiers in data science.",
                "key_takeaway": "Naive Bayes multiplies individual feature probabilities to classify text with extreme speed."
            }
        ],
        "visual_explainer": {
            "type": "diagram",
            "title": "Bayesian Probability Tree",
            "subtitle": "Prior Probability -> Likelihood of Evidence -> Posterior Probability",
            "diagram_type": "bayesian_tree",
            "parameters": {"prior_spam": 0.1, "evidence_hit": 0.95}
        },
        "code_example": {
            "title": "Calculating Posterior Probability with Bayes' Theorem",
            "language": "python",
            "code": "# Scenario: Medical diagnostic test\n# Disease prevalence in population (Prior): 1%\np_disease = 0.01\np_healthy = 0.99\n\n# Test accuracy:\n# True Positive Rate (Sensitivity): Test is positive given patient HAS disease = 99%\np_pos_given_disease = 0.99\n# False Positive Rate: Test is positive given patient is HEALTHY = 5%\np_pos_given_healthy = 0.05\n\n# Total probability of testing positive P(Pos)\np_pos = (p_pos_given_disease * p_disease) + (p_pos_given_healthy * p_healthy)\n\n# Bayes Theorem: P(Disease | Positive Test Result)\np_disease_given_pos = (p_pos_given_disease * p_disease) / p_pos\n\nprint(f\"Prior probability of disease:               {p_disease*100:.1f}%\")\nprint(f\"Posterior probability after testing positive: {p_disease_given_pos*100:.1f}%\")",
            "explanation": "Demonstrates why a positive test result on a rare condition results in ~16.6% actual infection probability due to base rates.",
            "output_preview": "Prior probability of disease:               1.0%\nPosterior probability after testing positive: 16.6%"
        },
        "quiz_id": "quiz-math-probability-bayes-theorem",
        "summary": "You mastered Bayes' Theorem and learned how machine learning updates predictions with incoming evidence.",
        "next_lesson_slug": "ml-linear-regression-ols",
        "prev_lesson_slug": "math-chain-rule-backprop-math"
    },

    # =========================================================================
    # COURSE 3: MACHINE LEARNING FUNDAMENTALS
    # =========================================================================
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
                "content_markdown": "To measure how well our line fits the data, we calculate the **Mean Squared Error (MSE)**:\n1. Find the gap (residual) between predicted value and true value: $(\\hat{y} - y)$.\n2. Square the gap so negative errors don't cancel positive errors: $(\\hat{y} - y)^2$.\n3. Take the average across all training data points:\n\n$$MSE = \\frac{1}{N} \\sum_{i=1}^N (y_{pred}^{(i)} - y_{true}^{(i)})^2$$\n\nA lower MSE score means our line makes much more accurate predictions.",
                "key_takeaway": "Squaring errors heavily penalizes large mistakes, pushing the model to fit all points evenly."
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
            "code": "import numpy as np\n\n# Sample dataset: House size (X) and Price (y)\nnp.random.seed(42)\nX = np.array([[1.0], [2.0], [3.0], [4.0]])\ny = np.array([[6.5], [9.0], [11.5], [14.0]])\n\n# Initialize starting parameters\nw = 0.0\nb = 0.0\nlearning_rate = 0.05\nepochs = 100\nN = len(X)\n\nfor epoch in range(epochs):\n    # 1. Make predictions\n    y_pred = w * X + b\n    # 2. Compute error gradients\n    dw = (2 / N) * np.sum((y_pred - y) * X)\n    db = (2 / N) * np.sum(y_pred - y)\n    # 3. Update parameters downhill\n    w -= learning_rate * dw\n    b -= learning_rate * db\n\nprint(f\"Learned Weight (w): {w:.2f} (Target: ~2.50)\")\nprint(f\"Learned Bias (b):   {b:.2f} (Target: ~4.00)\")",
            "explanation": "Illustrates the complete optimization loop of Gradient Descent tuning weight w and bias b to fit the points.",
            "output_preview": "Learned Weight (w): 2.47 (Target: ~2.50)\nLearned Bias (b):   4.08 (Target: ~4.00)"
        },
        "quiz_id": "quiz-ml-linear-regression-ols",
        "summary": "You learned how linear regression fits lines to data points and minimizes Mean Squared Error.",
        "next_lesson_slug": "ml-gradient-descent-intuition",
        "prev_lesson_slug": "math-probability-bayes-theorem"
    },
    {
        "slug": "ml-gradient-descent-intuition",
        "course_slug": "ml-fundamentals",
        "module_id": "ml-mod-1",
        "title": "Gradient Descent: Walking Down Foggy Mountains to Zero Error",
        "order": 2,
        "estimated_minutes": 20,
        "difficulty": "Beginner",
        "skill_tag": "optimization",
        "learning_objectives": [
            "Visualize the loss landscape as a hilly valley terrain where lowest altitude equals lowest error.",
            "Understand Learning Rate (alpha): Why too big overshoots and too small crawls.",
            "Compare Batch, Mini-Batch, and Stochastic Gradient Descent (SGD)."
        ],
        "theory_sections": [
            {
                "title": "The Blind Hiker in the Fog",
                "content_markdown": "Imagine you are dropped on a foggy mountain peak and need to find the lowest valley lake.\n* You can't see the lake through the dense fog.\n* But you can feel the slope of the ground right under your boots!\n* If the ground slopes downward to your left, you take a step to your left.\n\n**That is Gradient Descent**: At every step, the algorithm feels the slope of the loss function and takes a step in the steepest downward direction.",
                "key_takeaway": "Gradient Descent navigates complex loss surfaces by taking small steps downhill at each iteration."
            },
            {
                "title": "The Importance of Learning Rate (α)",
                "content_markdown": "The **Learning Rate** determines how big each step is:\n* **Too Small ($\alpha = 0.00001$)**: The hiker takes microscopic baby steps. Training takes hours or days to converge.\n* **Too Large ($\alpha = 5.0$)**: The hiker leaps so far they bounce across mountain peaks, causing the loss to explode to infinity (`NaN`)!\n* **Just Right ($\alpha = 0.01$)**: Steady, fast progress down to the valley floor.",
                "key_takeaway": "Always tune the learning rate first when training machine learning and deep learning models."
            }
        ],
        "visual_explainer": {
            "type": "chart",
            "title": "Learning Rate Convergence Comparison",
            "subtitle": "Small vs Ideal vs Overshooting Learning Rate curves",
            "diagram_type": "learning_rate_curves",
            "parameters": {"lr_small": 0.001, "lr_ideal": 0.05, "lr_large": 1.2}
        },
        "code_example": {
            "title": "Comparing Learning Rates on a 1D Quadratic Loss",
            "language": "python",
            "code": "def run_gd(lr, steps=5):\n    w = 10.0  # Start far from optimum (w=0)\n    trajectory = [w]\n    for _ in range(steps):\n        grad = 2 * w  # Derivative of w^2\n        w = w - lr * grad\n        trajectory.append(round(w, 2))\n    return trajectory\n\nprint(\"Ideal LR (0.1):      \", run_gd(0.1))\nprint(\"Too Small LR (0.01): \", run_gd(0.01))\nprint(\"Too Large LR (1.05): \", run_gd(1.05))",
            "explanation": "Demonstrates stable convergence vs slow crawl vs exploding divergence depending on step size.",
            "output_preview": "Ideal LR (0.1):       [10.0, 8.0, 6.4, 5.12, 4.1, 3.28]\nToo Small LR (0.01):  [10.0, 9.8, 9.6, 9.41, 9.22, 9.04]\nToo Large LR (1.05):  [10.0, -11.0, 12.1, -13.31, 14.64, -16.11]"
        },
        "quiz_id": "quiz-ml-gradient-descent-intuition",
        "summary": "You understood how gradient descent optimizes parameters and how learning rate controls convergence speed.",
        "next_lesson_slug": "ml-logistic-regression-classification",
        "prev_lesson_slug": "ml-linear-regression-ols"
    },
    {
        "slug": "ml-logistic-regression-classification",
        "course_slug": "ml-fundamentals",
        "module_id": "ml-mod-2",
        "title": "Logistic Regression: The S-Curve for Yes/No Decisions",
        "order": 3,
        "estimated_minutes": 25,
        "difficulty": "Beginner",
        "skill_tag": "classification",
        "learning_objectives": [
            "Learn why standard linear lines fail at classifying Yes/No (0 or 1) binary outcomes.",
            "Understand the Sigmoid activation function: Squeezing any number into a 0% to 100% probability.",
            "Master Decision Boundaries: Choosing threshold cutoffs (e.g. p > 0.5 -> Class 1)."
        ],
        "theory_sections": [
            {
                "title": "Why Can't We Use a Straight Line for Yes/No?",
                "content_markdown": "If you try to fit a straight line to predict whether a tumor is malignant ($1$) or benign ($0$), large tumor values will produce predicted numbers like $2.5$ or $-1.2$!\n\nProbabilities must always stay strictly between **0.0 (0%) and 1.0 (100%)**.",
                "key_takeaway": "Straight lines don't work for binary classification because predictions can exceed 0 and 1."
            },
            {
                "title": "The Sigmoid S-Curve",
                "content_markdown": "To fix this, we pass the linear output through the **Sigmoid function** $\\sigma(z)$:\n\n$$\\sigma(z) = \\frac{1}{1 + e^{-z}}$$\n\n* If $z = 0$, $\\sigma(0) = 0.5$ (50% toss-up)\n* If $z = +10$, $\\sigma(10) \\approx 0.9999$ (99.99% Yes!)\n* If $z = -10$, $\\sigma(-10) \\approx 0.0001$ (0.01% No!)\n\nIt bends the straight line into a smooth **S-shaped curve** that guarantees valid probabilities.",
                "key_takeaway": "Sigmoid squashes any input number into a valid probability between 0 and 1."
            }
        ],
        "visual_explainer": {
            "type": "chart",
            "title": "Sigmoid Probability Curve & Decision Threshold",
            "subtitle": "Binary data points with S-curve transition at z = 0",
            "diagram_type": "sigmoid_curve",
            "parameters": {"threshold": 0.5}
        },
        "code_example": {
            "title": "Classifying Pass/Fail Exam Results with Sigmoid",
            "language": "python",
            "code": "import numpy as np\n\ndef sigmoid(z):\n    return 1.0 / (1.0 + np.exp(-z))\n\n# Trained weights for exam prediction\n# z = (0.8 * study_hours) - 4.0\nstudy_hours = np.array([1.0, 3.0, 5.0, 8.0, 10.0])\nz = 0.8 * study_hours - 4.0\nprobabilities = sigmoid(z)\n\nfor hours, prob in zip(study_hours, probabilities):\n    prediction = \"PASS\" if prob >= 0.5 else \"FAIL\"\n    print(f\"Studied {hours:4.1f} hrs -> Pass Probability: {prob*100:5.1f}% -> Decision: {prediction}\")",
            "explanation": "Calculates pass/fail probabilities using Sigmoid with a 0.5 decision threshold.",
            "output_preview": "Studied  1.0 hrs -> Pass Probability:   3.9% -> Decision: FAIL\nStudied  3.0 hrs -> Pass Probability:  16.8% -> Decision: FAIL\nStudied  5.0 hrs -> Pass Probability:  50.0% -> Decision: PASS\nStudied  8.0 hrs -> Pass Probability:  91.7% -> Decision: PASS\nStudied 10.0 hrs -> Pass Probability:  98.2% -> Decision: PASS"
        },
        "quiz_id": "quiz-ml-logistic-regression-classification",
        "summary": "You mastered Logistic Regression and learned how Sigmoid squashes numbers into Yes/No probabilities.",
        "next_lesson_slug": "ml-decision-trees-entropy",
        "prev_lesson_slug": "ml-gradient-descent-intuition"
    },
    {
        "slug": "ml-decision-trees-entropy",
        "course_slug": "ml-fundamentals",
        "module_id": "ml-mod-2",
        "title": "Decision Trees: Asking 20 Smart Questions with Entropy",
        "order": 4,
        "estimated_minutes": 20,
        "difficulty": "Beginner",
        "skill_tag": "decision_trees",
        "learning_objectives": [
            "Understand Decision Trees as flowcharts of sequential Yes/No questions.",
            "Understand Entropy (measure of disorder/impurity) and Information Gain.",
            "Learn why Random Forests combine hundreds of trees to prevent overfitting."
        ],
        "theory_sections": [
            {
                "title": "The 20 Questions Game",
                "content_markdown": "When you play the game *'20 Questions'*, you don't guess random animals immediately. You ask broad questions that split the possibilities in half:\n1. *'Is it a mammal?'*\n2. *'Does it live in water?'*\n\n**A Decision Tree builds this exact question flowchart automatically from your data!** It evaluates every feature and picks the split that separates the classes most cleanly.",
                "key_takeaway": "Decision trees create intuitive flowchart rules that are easy for humans to interpret."
            },
            {
                "title": "Measuring Chaos: Entropy & Information Gain",
                "content_markdown": "**Entropy** measures how mixed up a basket of data is:\n* If a basket contains **10 Red apples and 0 Green apples**: Entropy is **0.0 (Pure)**.\n* If a basket contains **5 Red apples and 5 Green apples**: Entropy is **1.0 (Maximum Chaos)**.\n\nAt each branch, the tree chooses the question that produces the biggest drop in entropy (**Information Gain**).",
                "key_takeaway": "Trees pick splits that maximize purity (drop entropy to near zero)."
            }
        ],
        "visual_explainer": {
            "type": "diagram",
            "title": "Interactive Decision Tree Flowchart",
            "subtitle": "Root Node -> Branch Splitting -> Pure Leaf Predictions",
            "diagram_type": "decision_tree_hierarchy",
            "parameters": {"depth": 3, "features": ["Age > 30", "Income > 50k"]}
        },
        "code_example": {
            "title": "Calculating Shannon Entropy in Python",
            "language": "python",
            "code": "import numpy as np\n\ndef calculate_entropy(labels):\n    \"\"\"Calculates Shannon Entropy for a list of class labels.\"\"\"\n    _, counts = np.unique(labels, return_counts=True)\n    probabilities = counts / len(labels)\n    # Entropy = - sum(p * log2(p))\n    return -np.sum([p * np.log2(p) for p in probabilities if p > 0])\n\npure_set = ['Cat', 'Cat', 'Cat', 'Cat']\nmixed_set = ['Cat', 'Dog', 'Cat', 'Dog']\n\nprint(f\"Entropy of Pure Basket:  {calculate_entropy(pure_set):.4f} (Zero Chaos)\")\nprint(f\"Entropy of 50/50 Basket: {calculate_entropy(mixed_set):.4f} (Maximum Uncertainty)\")",
            "explanation": "Demonstrates entropy calculation showing 0 for perfectly pure sets and 1.0 for equally split sets.",
            "output_preview": "Entropy of Pure Basket:  0.0000 (Zero Chaos)\nEntropy of 50/50 Basket: 1.0000 (Maximum Uncertainty)"
        },
        "quiz_id": "quiz-ml-decision-trees-entropy",
        "summary": "You understood how decision trees split data using entropy and information gain.",
        "next_lesson_slug": "ml-kmeans-clustering-algorithm",
        "prev_lesson_slug": "ml-logistic-regression-classification"
    },
    {
        "slug": "ml-kmeans-clustering-algorithm",
        "course_slug": "ml-fundamentals",
        "module_id": "ml-mod-3",
        "title": "K-Means Clustering: Finding Natural Groups in Unlabeled Data",
        "order": 5,
        "estimated_minutes": 20,
        "difficulty": "Beginner",
        "skill_tag": "clustering",
        "learning_objectives": [
            "Understand Unsupervised Learning: Discovering patterns without teacher labels.",
            "Learn the 3-step K-Means dance: Assign points, recalculate centroids, repeat.",
            "Use the Elbow Method to choose the ideal number of clusters (K)."
        ],
        "theory_sections": [
            {
                "title": "Clustering: Grouping Without Labels",
                "content_markdown": "In Supervised Learning, every training row has a teacher label (e.g. *'Spam'* or *'Not Spam'*).\n\nIn **Unsupervised Learning**, we have raw unlabeled data—like 100,000 customer shopping receipts. **K-Means clustering** groups these customers into $K$ distinct personas (e.g. *Budget Shoppers*, *Tech Enthusiasts*, *Weekend Bargain Hunters*) based on distance similarity.",
                "key_takeaway": "K-Means discovers natural groupings in raw data without needing human labels."
            },
            {
                "title": "The K-Means Dance in 3 Steps",
                "content_markdown": "1. **Initialize**: Drop $K$ random pins (centroids) on the scatter plot.\n2. **Assign**: Each data point joins the closest pin.\n3. **Update**: Move each pin to the exact center average of its newly joined points.\n\nRepeat steps 2 and 3 until the pins stop moving!",
                "key_takeaway": "K-Means converges rapidly by alternating between assigning points and recentering centroids."
            }
        ],
        "visual_explainer": {
            "type": "simulation_preview",
            "title": "K-Means 2D Voronoi Clustering",
            "subtitle": "Data points colored by nearest moving centroid",
            "diagram_type": "kmeans_voronoi",
            "parameters": {"k": 3, "iterations": 8}
        },
        "code_example": {
            "title": "Simple 1D K-Means Clustering Implementation",
            "language": "python",
            "code": "import numpy as np\n\n# 1D Customer spending scores\ndata = np.array([10, 12, 15, 80, 85, 90])\n\n# Initialize 2 cluster centroids\nc1, c2 = 10.0, 50.0\n\nfor iteration in range(3):\n    # 1. Assign points to closest centroid\n    group1 = [x for x in data if abs(x - c1) <= abs(x - c2)]\n    group2 = [x for x in data if abs(x - c2) < abs(x - c1)]\n    \n    # 2. Recalculate centroids as mean of groups\n    c1 = np.mean(group1)\n    c2 = np.mean(group2)\n    print(f\"Iter {iteration+1}: Centroid 1={c1:4.1f} (Group: {group1}), Centroid 2={c2:4.1f} (Group: {group2})\")",
            "explanation": "Illustrates the iterative assignment and recentering of cluster centers.",
            "output_preview": "Iter 1: Centroid 1=12.3 (Group: [10, 12, 15]), Centroid 2=85.0 (Group: [80, 85, 90])\nIter 2: Centroid 1=12.3 (Group: [10, 12, 15]), Centroid 2=85.0 (Group: [80, 85, 90])\nIter 3: Centroid 1=12.3 (Group: [10, 12, 15]), Centroid 2=85.0 (Group: [80, 85, 90])"
        },
        "quiz_id": "quiz-ml-kmeans-clustering-algorithm",
        "summary": "You understood unsupervised clustering and how K-Means finds clusters using distance minimization.",
        "next_lesson_slug": "dl-perceptron-forward-prop",
        "prev_lesson_slug": "ml-decision-trees-entropy"
    },

    # =========================================================================
    # COURSE 4: DEEP LEARNING & NEURAL NETWORKS
    # =========================================================================
    {
        "slug": "dl-perceptron-forward-prop",
        "course_slug": "deep-learning-fundamentals",
        "module_id": "dl-mod-1",
        "title": "Artificial Neurons, Layers & Forward Propagation",
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
                "content_markdown": "If we only did addition and multiplication, stacking 100 neural layers would still just equal one giant straight line!\n\n**Activation functions (like ReLU or Sigmoid)** introduce curves and bends. For example, **ReLU** (Rectified Linear Unit) has a simple rule:\n\n$$\\text{ReLU}(z) = \\max(0, z)$$\n\nIf input $z$ is negative, output `0`. If positive, output $z$. This simple on/off switch enables deep networks to bend decision boundaries around complex shapes like circles, faces, and speech patterns.",
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
            "code": "import numpy as np\n\ndef relu(z):\n    \"\"\"Zero out negative values, keep positive values unchanged.\"\"\"\n    return np.maximum(0, z)\n\n# 2 input samples with 3 features each\nX = np.array([\n    [1.0, 2.0, -1.0],\n    [0.5, -1.5, 2.0]\n])\n\n# Layer 1 weights: 3 inputs -> 4 hidden neurons\nnp.random.seed(42)\nW1 = np.random.randn(3, 4) * 0.1\nb1 = np.zeros((1, 4))\n\n# Forward pass through Layer 1\nZ1 = np.dot(X, W1) + b1\nA1 = relu(Z1)  # Apply ReLU activation\n\nprint(\"Input batch shape:\", X.shape)\nprint(\"Hidden layer activation shape:\", A1.shape)\nprint(\"Sample 0 activations:\\n\", np.round(A1[0], 3))",
            "explanation": "Demonstrates matrix multiplication followed by non-linear ReLU activation for a hidden layer.",
            "output_preview": "Input batch shape: (2, 3)\nHidden layer activation shape: (2, 4)\nSample 0 activations:\n [0.082 0.    0.145 0.   ]"
        },
        "quiz_id": "quiz-dl-perceptron-forward-prop",
        "summary": "You explored artificial neurons, why non-linear activations are necessary, and how layers pass signals forward.",
        "next_lesson_slug": "dl-activation-functions",
        "prev_lesson_slug": "ml-kmeans-clustering-algorithm"
    },
    {
        "slug": "dl-activation-functions",
        "course_slug": "deep-learning-fundamentals",
        "module_id": "dl-mod-1",
        "title": "Activation Functions Showdown: ReLU, Leaky ReLU, Sigmoid & Softmax",
        "order": 2,
        "estimated_minutes": 20,
        "difficulty": "Intermediate",
        "skill_tag": "neural_networks",
        "learning_objectives": [
            "Understand why ReLU became the default activation choice for modern deep learning.",
            "Learn what the 'Dying ReLU' problem is and how Leaky ReLU fixes it.",
            "Use Softmax on the final output layer to produce multi-class probability distributions."
        ],
        "theory_sections": [
            {
                "title": "Why Did ReLU Replace Sigmoid in Deep Networks?",
                "content_markdown": "In early neural networks, researchers used Sigmoid for every hidden layer. But Sigmoid flattens out near 0 and 1, where its derivative becomes practically zero.\n\nIn a 20-layer network, multiplying 20 tiny derivatives together causes the gradient to shrink to `0.000000001` (**Vanishing Gradient Problem**)—freezing learning in early layers!\n\n**ReLU (Rectified Linear Unit)** fixed this: its slope is always **1.0** for all positive numbers, allowing gradients to flow effortlessly across hundreds of layers.",
                "key_takeaway": "ReLU prevents vanishing gradients and computes 10x faster than exponential activations."
            },
            {
                "title": "Softmax: Multi-Class Probabilities",
                "content_markdown": "When classifying images into 3 or more categories (e.g. Dog, Cat, Bird), the output layer uses **Softmax**:\n\n$$\\text{Softmax}(z_i) = \\frac{e^{z_i}}{\\sum_{j} e^{z_j}}$$\n\nIt turns raw scores (logits) into clean probabilities that are guaranteed to sum up to exactly **1.0 (100%)**.",
                "key_takeaway": "Use ReLU for hidden layers and Softmax for the final multi-class output layer."
            }
        ],
        "visual_explainer": {
            "type": "chart",
            "title": "Activation Function Comparison Curves",
            "subtitle": "ReLU vs Leaky ReLU vs Sigmoid vs Tanh",
            "diagram_type": "activation_curves",
            "parameters": {"functions": ["ReLU", "Sigmoid", "Tanh", "LeakyReLU"]}
        },
        "code_example": {
            "title": "Comparing Activations and Computing Softmax Probabilities",
            "language": "python",
            "code": "import numpy as np\n\ndef softmax(logits):\n    exp_vals = np.exp(logits - np.max(logits))  # subtract max for numerical stability\n    return exp_vals / np.sum(exp_vals)\n\n# Raw output logits from a network for [Cat, Dog, Bird]\nraw_logits = np.array([2.5, 1.0, 0.2])\nprobabilities = softmax(raw_logits)\n\nprint(\"Raw Model Logits:     \", raw_logits)\nprint(\"Softmax Probabilities: \", np.round(probabilities, 3))\nprint(f\"Sum of Probabilities:  {np.sum(probabilities):.2f}\")\nprint(f\"Winning Prediction:    Class {np.argmax(probabilities)} (Confidence: {np.max(probabilities)*100:.1f}%)\")",
            "explanation": "Demonstrates converting unbounded network logits into normalized class probabilities.",
            "output_preview": "Raw Model Logits:      [2.5 1.  0.2]\nSoftmax Probabilities:  [0.751 0.168 0.081]\nSum of Probabilities:   1.00\nWinning Prediction:     Class 0 (Confidence: 75.1%)"
        },
        "quiz_id": "quiz-dl-activation-functions",
        "summary": "You compared major activation functions and learned why ReLU and Softmax are the modern industry standards.",
        "next_lesson_slug": "dl-backpropagation-calculus",
        "prev_lesson_slug": "dl-perceptron-forward-prop"
    },
    {
        "slug": "dl-backpropagation-calculus",
        "course_slug": "deep-learning-fundamentals",
        "module_id": "dl-mod-2",
        "title": "Backpropagation Demystified: How Neural Networks Learn from Mistakes",
        "order": 3,
        "estimated_minutes": 30,
        "difficulty": "Intermediate",
        "skill_tag": "backpropagation",
        "learning_objectives": [
            "Understand the training feedback loop: Forward pass -> Loss calculation -> Backward pass -> Weight update.",
            "Learn how error signals are passed backwards through each neuron proportionally to its contribution.",
            "Build an intuitive mental model of automatic differentiation."
        ],
        "theory_sections": [
            {
                "title": "Assigning Blame Backwards",
                "content_markdown": "Imagine a restaurant with a Head Chef (output layer), Sous Chefs (hidden layers), and Prep Cooks (input layer).\n\nIf a customer sends soup back because it's way too salty (High Loss), the Head Chef looks at the Sous Chef who seasoned it, who in turn looks at the Prep Cook who measured the salt.\n\n**Backpropagation is this blame assignment process**: It computes how much each neuron in every layer contributed to the final mistake so each weight can be adjusted.",
                "key_takeaway": "Backpropagation distributes credit and blame backwards through every layer using the chain rule."
            },
            {
                "title": "The 4 Steps of Training",
                "content_markdown": "1. **Forward Pass**: Feed inputs through weights to make a prediction $\\hat{y}$.\n2. **Loss Computation**: Measure how wrong the prediction was ($Loss = (\\hat{y} - y)^2$).\n3. **Backward Pass (Backprop)**: Compute $\\frac{\\partial Loss}{\\partial W}$ for every weight using the chain rule.\n4. **Optimizer Step**: Update weights downhill ($W \\leftarrow W - \\alpha \\cdot \\nabla W$).",
                "key_takeaway": "Repeating this 4-step loop thousands of times turns a random network into an intelligent classifier."
            }
        ],
        "visual_explainer": {
            "type": "diagram",
            "title": "Backpropagation Gradient Flow",
            "subtitle": "Error delta propagating backwards across dense layers",
            "diagram_type": "backprop_graph"
        },
        "code_example": {
            "title": "Complete 1-Neuron Backpropagation from Scratch in Python",
            "language": "python",
            "code": "import numpy as np\n\n# Single training sample: Input x=2.0, True Target y=10.0\nx = 2.0\ntarget = 10.0\n\n# Starting weight & bias\nw = 1.0\nb = 0.0\nlr = 0.1\n\nprint(f\"Initial: w={w:.2f}, b={b:.2f}\")\nfor step in range(4):\n    # 1. Forward Pass\n    y_pred = w * x + b\n    loss = (y_pred - target) ** 2\n    \n    # 2. Backward Pass (Chain Rule)\n    dloss_dpred = 2 * (y_pred - target)  # dLoss/dY_hat\n    dpred_dw = x                         # dY_hat/dw\n    dpred_db = 1.0                       # dY_hat/db\n    \n    dw = dloss_dpred * dpred_dw\n    db = dloss_dpred * dpred_db\n    \n    # 3. Update\n    w -= lr * dw\n    b -= lr * db\n    print(f\"Step {step+1}: Loss={loss:6.2f} -> New w={w:.2f}, New b={b:.2f}\")",
            "explanation": "Demonstrates forward pass, chain rule derivative calculation, and gradient descent update step.",
            "output_preview": "Initial: w=1.00, b=0.00\nStep 1: Loss= 64.00 -> New w=4.20, New b=1.60\nStep 2: Loss=  0.00 -> New w=4.20, New b=1.60\nStep 3: Loss=  0.00 -> New w=4.20, New b=1.60\nStep 4: Loss=  0.00 -> New w=4.20, New b=1.60"
        },
        "quiz_id": "quiz-dl-backpropagation-calculus",
        "summary": "You understood the full Backpropagation loop and how error gradients adjust network weights.",
        "next_lesson_slug": "dl-cnn-convolution-pooling",
        "prev_lesson_slug": "dl-activation-functions"
    },
    {
        "slug": "dl-cnn-convolution-pooling",
        "course_slug": "deep-learning-fundamentals",
        "module_id": "dl-mod-3",
        "title": "Convolutional Neural Networks (CNNs): How Computers 'See' Images",
        "order": 4,
        "estimated_minutes": 25,
        "difficulty": "Intermediate",
        "skill_tag": "computer_vision",
        "learning_objectives": [
            "Understand why standard dense networks fail on large images (parameter explosion and losing spatial relations).",
            "Learn how sliding 2D convolution filters detect edges, textures, and object parts.",
            "Understand Max Pooling for spatial downsampling and translation invariance."
        ],
        "theory_sections": [
            {
                "title": "The Flashlight Analogy (Convolution Filter)",
                "content_markdown": "Imagine holding a small 3x3 square flashlight over a dark photograph.\n* You slide the flashlight across the picture row by row.\n* If the 3x3 patch under your flashlight matches an edge pattern, the flashlight glows brightly (high activation).\n* If it's blank wall, the flashlight stays dim.\n\n**A Convolutional Filter (Kernel)** is this 3x3 pattern detector! Early layers detect simple lines and curves, middle layers detect eyes and wheels, and deep layers recognize whole faces and cars.",
                "key_takeaway": "Convolution filters slide across images to extract visual features regardless of where they appear."
            },
            {
                "title": "Max Pooling: Compressing Without Losing Key Details",
                "content_markdown": "**Max Pooling** looks at each 2x2 patch of a feature map and keeps only the **maximum number**.\n\nThis cuts image dimensions in half (reducing memory by 75%) while preserving the strongest detected features, making the network invariant to small shifts or rotations.",
                "key_takeaway": "Max Pooling downsamples feature maps to reduce computation and improve generalization."
            }
        ],
        "visual_explainer": {
            "type": "simulation_preview",
            "title": "2D Convolution Kernel Sliding & Feature Map",
            "subtitle": "3x3 filter scanning a 5x5 input matrix to produce a feature map",
            "diagram_type": "cnn_kernel_stride",
            "parameters": {"kernel_size": 3, "stride": 1, "padding": 0}
        },
        "code_example": {
            "title": "Applying a Vertical Edge Detection Filter in NumPy",
            "language": "python",
            "code": "import numpy as np\n\n# 4x4 grayscale image with a vertical bright stripe down the middle\nimage = np.array([\n    [0, 10, 10, 0],\n    [0, 10, 10, 0],\n    [0, 10, 10, 0],\n    [0, 10, 10, 0]\n])\n\n# 3x3 Sobel vertical edge detection filter\nkernel = np.array([\n    [-1, 0, 1],\n    [-2, 0, 2],\n    [-1, 0, 1]\n])\n\n# Manual 2D convolution over the top-left 3x3 patch\npatch = image[0:3, 0:3]\nedge_score = np.sum(patch * kernel)\n\nprint(\"Image 3x3 Patch:\\n\", patch)\nprint(\"Filter Kernel:\\n\", kernel)\nprint(f\"Convolution Result for patch: {edge_score} (Strong Edge Detected!)\")",
            "explanation": "Demonstrates how multiplying an image patch with a filter matrix detects the presence of vertical edges.",
            "output_preview": "Image 3x3 Patch:\n [[ 0 10 10]\n  [ 0 10 10]\n  [ 0 10 10]]\nFilter Kernel:\n [[-1  0  1]\n  [-2  0  2]\n  [-1  0  1]]\nConvolution Result for patch: 40 (Strong Edge Detected!)"
        },
        "quiz_id": "quiz-dl-cnn-convolution-pooling",
        "summary": "You understood convolutional filters, feature map hierarchies, and max pooling in Computer Vision.",
        "next_lesson_slug": "genai-tokenization-embeddings",
        "prev_lesson_slug": "dl-backpropagation-calculus"
    },

    # =========================================================================
    # COURSE 5: GENERATIVE AI, TRANSFORMERS & LLMS
    # =========================================================================
    {
        "slug": "genai-tokenization-embeddings",
        "course_slug": "generative-ai-fundamentals",
        "module_id": "genai-mod-1",
        "title": "Words as Coordinates: Tokenization & Embedding Spaces",
        "order": 1,
        "estimated_minutes": 25,
        "difficulty": "Intermediate",
        "skill_tag": "nlp_embeddings",
        "learning_objectives": [
            "Learn how Byte-Pair Encoding (BPE) tokenizers break text into subword chunks.",
            "Understand Embedding Spaces: Mapping words into multidimensional coordinate maps.",
            "Explore Word Vector Math: King - Man + Woman = Queen."
        ],
        "theory_sections": [
            {
                "title": "How AI Reads: Tokenization",
                "content_markdown": "Computers don't read words or letters directly. A **tokenizer** chops sentences into subword tokens and assigns each one a unique integer ID.\n\n* *'unbelievable'* $\\rightarrow$ `['un', 'believ', 'able']` $\\rightarrow$ `[428, 19203, 502]`\n\nSubword tokenization allows modern LLMs to handle rare words, typos, code, and emojis without needing an infinite dictionary.",
                "key_takeaway": "Tokenizers turn raw text into lists of integer IDs."
            },
            {
                "title": "Embedding Space: The Mental Map of Words",
                "content_markdown": "An **Embedding** replaces each integer ID with a rich vector of numbers (e.g. 1,536 coordinates in GPT-4).\n\nIn this space, words with similar meanings live close together:\n* *'puppy'* and *'dog'* have almost identical coordinates.\n* Directions in space capture semantic concepts (e.g. Capital city, Gender, Verb tense).\n\n$$\\vec{v}_{\\text{King}} - \\vec{v}_{\\text{Man}} + \\vec{v}_{\\text{Woman}} \\approx \\vec{v}_{\\text{Queen}}$$",
                "key_takeaway": "Embeddings convert discrete words into smooth geometric coordinates where distance measures meaning."
            }
        ],
        "visual_explainer": {
            "type": "chart",
            "title": "2D Semantic Word Embedding Space",
            "subtitle": "Word vectors clustered by category (Animals, Royalty, Tech)",
            "diagram_type": "embedding_scatter",
            "parameters": {"clusters": ["Animals", "Royalty", "Countries"]}
        },
        "code_example": {
            "title": "Semantic Vector Arithmetic in Python",
            "language": "python",
            "code": "import numpy as np\n\n# Simulated 3D embeddings: [Royalty, Gender (M=+1, F=-1), Power]\nking   = np.array([0.9,  0.8, 0.9])\nman    = np.array([0.1,  0.9, 0.2])\nwoman  = np.array([0.1, -0.9, 0.2])\nqueen  = np.array([0.9, -0.8, 0.9])\napple  = np.array([0.0,  0.0, -0.9])\n\n# Word Math: King - Man + Woman\nresult_vector = king - man + woman\n\ndef similarity(a, b):\n    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))\n\nprint(\"Similarity to Queen:\", round(similarity(result_vector, queen), 4))\nprint(\"Similarity to Apple:\", round(similarity(result_vector, apple), 4))",
            "explanation": "Demonstrates how vector addition and subtraction preserves semantic relationships.",
            "output_preview": "Similarity to Queen: 0.9945 (Near Perfect Match!)\nSimilarity to Apple: -0.6015 (Unrelated)"
        },
        "quiz_id": "quiz-genai-tokenization-embeddings",
        "summary": "You explored subword tokenization and learned how embedding spaces capture word meanings geometrically.",
        "next_lesson_slug": "genai-self-attention-transformers",
        "prev_lesson_slug": "dl-cnn-convolution-pooling"
    },
    {
        "slug": "genai-self-attention-transformers",
        "course_slug": "generative-ai-fundamentals",
        "module_id": "genai-mod-2",
        "title": "The Self-Attention Mechanism Behind ChatGPT",
        "order": 2,
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
        "next_lesson_slug": "genai-rag-architecture-pipeline",
        "prev_lesson_slug": "genai-tokenization-embeddings"
    },
    {
        "slug": "genai-rag-architecture-pipeline",
        "course_slug": "generative-ai-fundamentals",
        "module_id": "genai-mod-3",
        "title": "RAG (Retrieval-Augmented Generation): Giving LLMs Real-Time Memory",
        "order": 3,
        "estimated_minutes": 25,
        "difficulty": "Advanced",
        "skill_tag": "rag_systems",
        "learning_objectives": [
            "Understand the limitations of raw LLMs (knowledge cutoffs, hallucinations, private company data).",
            "Learn the complete RAG pipeline: Chunking -> Embedding -> Vector DB -> Prompt Injection -> LLM Answer.",
            "Explore semantic similarity search using cosine distance in Vector Databases."
        ],
        "theory_sections": [
            {
                "title": "Why Foundation Models Need RAG",
                "content_markdown": "Even the largest LLM suffers from two major problems:\n1. **Knowledge Cutoff**: It doesn't know what happened yesterday.\n2. **Private Data**: It has never seen your company's internal PDFs, HR manuals, or private codebases.\n\nInstead of retraining a $10M model, **RAG (Retrieval-Augmented Generation)** acts like an **open-book exam**: When a user asks a question, the system searches your private documents for relevant snippets and pastes them directly into the prompt!",
                "key_takeaway": "RAG eliminates hallucinations by grounding the LLM's response in verified document chunks."
            },
            {
                "title": "The 5-Step RAG Pipeline",
                "content_markdown": "1. **Chunk**: Split long PDF documents into 500-word paragraphs.\n2. **Embed**: Convert each chunk into an embedding vector using an embedding model.\n3. **Index**: Store all chunk vectors in a **Vector Database** (e.g. Chroma, Pinecone).\n4. **Retrieve**: When the user asks a question, embed their question and retrieve the Top-3 most similar chunks.\n5. **Generate**: Ask the LLM: *'Answer the question based ONLY on these 3 retrieved excerpts.'*",
                "key_takeaway": "Vector search retrieves relevant knowledge in milliseconds, which is then synthesized by the LLM."
            }
        ],
        "visual_explainer": {
            "type": "architecture_flow",
            "title": "End-to-End RAG Architecture",
            "subtitle": "User Query -> Vector Embed -> Vector DB Retrieval -> Prompt Context -> LLM Response",
            "diagram_type": "rag_pipeline"
        },
        "code_example": {
            "title": "Building an In-Memory Mini RAG System in Python",
            "language": "python",
            "code": "import numpy as np\n\n# Simulated knowledge base documents\ndocuments = [\n    \"Antigravity IDE includes built-in terminal, Monaco editor, and AI tutor.\",\n    \"The refund policy allows returns within 30 days of purchase.\",\n    \"Python 3.13 introduces experimental free-threaded execution without the GIL.\"\n]\n\n# Simplified 3D embedding vectors for each doc\n# Coordinates: [Software/IDE, Company Policy, Python Internals]\ndoc_embeddings = np.array([\n    [0.9, 0.1, 0.2],\n    [0.1, 0.9, 0.0],\n    [0.2, 0.0, 0.9]\n])\n\n# User query: 'How do I get my money back?'\nquery_embedding = np.array([0.05, 0.95, 0.0])\n\n# Calculate similarity to all documents\nsimilarities = [np.dot(query_embedding, doc) for doc in doc_embeddings]\nbest_idx = int(np.argmax(similarities))\n\nprint(f\"User Query: 'How do I get my money back?'\")\nprint(f\"Retrieved Document: \\\"{documents[best_idx]}\\\"\")\nprint(f\"Similarity Score:   {similarities[best_idx]:.4f}\")",
            "explanation": "Illustrates how vector cosine matching selects the most relevant document chunk to inject into the LLM prompt.",
            "output_preview": "User Query: 'How do I get my money back?'\nRetrieved Document: \"The refund policy allows returns within 30 days of purchase.\"\nSimilarity Score:   0.8600"
        },
        "quiz_id": "quiz-genai-rag-architecture-pipeline",
        "summary": "You understood how RAG systems combine vector similarity search with LLM reasoning to answer questions accurately.",
        "next_lesson_slug": "prompt-foundations-few-shot",
        "prev_lesson_slug": "genai-self-attention-transformers"
    },

    # =========================================================================
    # COURSE 6: PROMPT ENGINEERING & AI AGENTS
    # =========================================================================
    {
        "slug": "prompt-foundations-few-shot",
        "course_slug": "prompt-engineering-agents",
        "module_id": "agent-mod-1",
        "title": "Prompt Engineering Mastery: Few-Shot, System Prompts & Delimiters",
        "order": 1,
        "estimated_minutes": 20,
        "difficulty": "Beginner",
        "skill_tag": "prompt_engineering",
        "learning_objectives": [
            "Learn how System Prompts establish persistent role, tone, and guardrails for LLMs.",
            "Use clear delimiters (###, XML tags, ```) to prevent prompt injection and ambiguity.",
            "Apply Few-Shot Prompting: Providing 2-3 input/output examples to guarantee formatted responses."
        ],
        "theory_sections": [
            {
                "title": "Directing the Model: Roles & Delimiters",
                "content_markdown": "Large Language Models are probabilistic text prediction engines. If your instructions are vague, the model guesses what you want.\n\n**Three Essential Prompt Engineering Rules**:\n1. **Assign a Persona**: *'You are a senior compiler engineer explaining concepts to a college sophomore.'*\n2. **Use Clear Delimiters**: Enclose user text in `\"\"\"` or `<user_input>` so the model never confuses instructions with data.\n3. **Specify the Output Format**: Explicitly demand JSON, Markdown tables, or bullet lists.",
                "key_takeaway": "Clear delimiters and explicit personas dramatically reduce formatting errors."
            },
            {
                "title": "Zero-Shot vs Few-Shot Prompting",
                "content_markdown": "* **Zero-Shot**: Asking the model to perform a task with zero examples (*'Classify this sentiment'*).\n* **Few-Shot**: Giving the model 2 or 3 completed examples before the test input.\n\nProviding just 2 high-quality examples increases classification accuracy on difficult domain-specific tasks from ~65% to over **95%**.",
                "key_takeaway": "Few-shot examples teach the model your exact expected format and reasoning style."
            }
        ],
        "visual_explainer": {
            "type": "diagram",
            "title": "Few-Shot Prompt Structure",
            "subtitle": "System Prompt -> Example 1 (Input/Output) -> Example 2 (Input/Output) -> Target Query",
            "diagram_type": "prompt_anatomy"
        },
        "code_example": {
            "title": "Structuring a Robust Few-Shot Prompt in Python",
            "language": "python",
            "code": "def build_sentiment_prompt(user_review: str) -> str:\n    return f\"\"\"You are an automated customer feedback sentiment extractor.\nOutput ONLY valid JSON with keys: 'sentiment' (POSITIVE/NEGATIVE/NEUTRAL) and 'confidence' (0.0 - 1.0).\n\n### Examples:\nReview: 'The delivery arrived 3 days early and worked flawlessly!'\n{{\"sentiment\": \"POSITIVE\", \"confidence\": 0.98}}\n\nReview: 'It broke after 10 minutes of use. Very disappointed.'\n{{\"sentiment\": \"NEGATIVE\", \"confidence\": 0.95}}\n\n### New Task:\nReview: '{user_review}'\n\"\"\"\n\ntest_review = \"Great sound quality but battery life could be a little better.\"\nprint(build_sentiment_prompt(test_review))",
            "explanation": "Demonstrates clear formatting, system instructions, few-shot examples, and strict JSON output schemas.",
            "output_preview": "You are an automated customer feedback sentiment extractor.\nOutput ONLY valid JSON with keys: 'sentiment' (POSITIVE/NEGATIVE/NEUTRAL) and 'confidence' (0.0 - 1.0).\n\n### Examples:\nReview: 'The delivery arrived 3 days early and worked flawlessly!'\n{\"sentiment\": \"POSITIVE\", \"confidence\": 0.98}\n\nReview: 'It broke after 10 minutes of use. Very disappointed.'\n{\"sentiment\": \"NEGATIVE\", \"confidence\": 0.95}\n\n### New Task:\nReview: 'Great sound quality but battery life could be a little better.'"
        },
        "quiz_id": "quiz-prompt-foundations-few-shot",
        "summary": "You mastered system prompts, delimiters, and few-shot examples to reliably control AI output.",
        "next_lesson_slug": "prompt-chain-of-thought-reasoning",
        "prev_lesson_slug": "genai-rag-architecture-pipeline"
    },
    {
        "slug": "prompt-chain-of-thought-reasoning",
        "course_slug": "prompt-engineering-agents",
        "module_id": "agent-mod-2",
        "title": "Chain-of-Thought & Step-by-Step Reasoning",
        "order": 2,
        "estimated_minutes": 20,
        "difficulty": "Beginner",
        "skill_tag": "prompt_engineering",
        "learning_objectives": [
            "Learn why forcing LLMs to 'Think step-by-step' prevents mathematical and logical hallucinations.",
            "Understand Chain-of-Thought (CoT) prompting mechanics.",
            "Explore Self-Consistency: Generating multiple reasoning paths and taking the majority vote."
        ],
        "theory_sections": [
            {
                "title": "Why AI Fails at Immediate Answers",
                "content_markdown": "If you ask an LLM a complex riddle or word problem and demand an immediate 1-word answer, it often guesses incorrectly because it only generates one token at a time without 'planning'.\n\nWhen you instruct the model: **'Think step-by-step before stating your final answer'**, you give the model **working memory scratchpad space** (intermediate tokens) to work through math calculations and check logic.",
                "key_takeaway": "Encouraging step-by-step reasoning provides token scratchpad space that drastically improves accuracy on logic and math."
            },
            {
                "title": "Self-Consistency (Majority Voting)",
                "content_markdown": "For mission-critical answers, we run the reasoning prompt 5 times at temperature `0.7` and take the **majority vote** among the final answers.\n\nIf 4 out of 5 reasoning paths arrive at `$42.50`, we can be highly confident in the result.",
                "key_takeaway": "Self-consistency uses multiple reasoning passes to filter out random hallucinations."
            }
        ],
        "visual_explainer": {
            "type": "diagram",
            "title": "Chain of Thought Reasoning Tree",
            "subtitle": "Prompt -> Step 1 Deduction -> Step 2 Math Check -> Final Answer",
            "diagram_type": "chain_of_thought"
        },
        "code_example": {
            "title": "Chain-of-Thought Reasoning Template",
            "language": "python",
            "code": "problem = \"\"\"\nA bakery sells cupcakes for $3 each and cookies for $2 each.\nSarah bought 4 cupcakes and 6 cookies, and paid with a $50 bill.\nHow much change does she receive?\n\"\"\"\n\ncot_prompt = f\"\"\"Solve the following math problem step-by-step.\nFirst write out your deductions inside <thinking> tags.\nThen provide the final dollar amount inside <answer> tags.\n\nProblem:\n{problem}\n\"\"\"\n\nprint(cot_prompt)",
            "explanation": "Illustrates how structured thinking tags encourage reasoning transparency and accurate final deductions.",
            "output_preview": "Solve the following math problem step-by-step.\nFirst write out your deductions inside <thinking> tags.\nThen provide the final dollar amount inside <answer> tags.\n\nProblem:\nA bakery sells cupcakes for $3 each and cookies for $2 each.\nSarah bought 4 cupcakes and 6 cookies, and paid with a $50 bill.\nHow much change does she receive?"
        },
        "quiz_id": "quiz-prompt-chain-of-thought-reasoning",
        "summary": "You understood Chain-of-Thought prompting and why step-by-step scratchpad tokens resolve complex reasoning tasks.",
        "next_lesson_slug": "prompt-ai-agents-tool-use",
        "prev_lesson_slug": "prompt-foundations-few-shot"
    },
    {
        "slug": "prompt-ai-agents-tool-use",
        "course_slug": "prompt-engineering-agents",
        "module_id": "agent-mod-3",
        "title": "Building Autonomous AI Agents: Function Calling & ReAct Loops",
        "order": 3,
        "estimated_minutes": 25,
        "difficulty": "Intermediate",
        "skill_tag": "ai_agents",
        "learning_objectives": [
            "Understand the difference between a static Chatbot and an Autonomous Agent.",
            "Learn the ReAct loop: Thought -> Action (Tool Call) -> Observation (Tool Output) -> Final Response.",
            "Understand Function Calling: Letting LLMs output structured JSON to invoke APIs and databases."
        ],
        "theory_sections": [
            {
                "title": "From Chatbots to Agents",
                "content_markdown": "A traditional chatbot can only talk.\n\nAn **AI Agent can take actions in the real world**! It can:\n* Search the web for current weather or stock prices\n* Query a SQL database to look up order status\n* Execute Python code in a sandbox to plot graphs\n* Send emails and update calendar invites",
                "key_takeaway": "Agents combine reasoning with external tool execution to solve multi-step problems autonomously."
            },
            {
                "title": "The ReAct (Reason + Act) Loop",
                "content_markdown": "How does an agent solve a goal like *'Check tomorrow's weather in Tokyo and tell me if I need an umbrella'?*\n\n1. **Thought**: *'I need to look up Tokyo's weather forecast for tomorrow.'*\n2. **Action**: Call tool `get_weather(city=\"Tokyo\", date=\"tomorrow\")`\n3. **Observation**: Tool returns `{\"rain_chance\": 85%, \"condition\": \"Heavy Rain\"}`\n4. **Thought**: *'Rain chance is 85%, which is very high. I should recommend an umbrella.'*\n5. **Final Answer**: *'Yes, bring an umbrella! Tokyo has an 85% chance of heavy rain tomorrow.'*",
                "key_takeaway": "The ReAct loop allows agents to repeatedly think, invoke tools, inspect outputs, and formulate answers."
            }
        ],
        "visual_explainer": {
            "type": "architecture_flow",
            "title": "Autonomous Agent ReAct Loop",
            "subtitle": "User Goal -> LLM Thought -> Tool Execution -> Observation -> Loop -> Final Answer",
            "diagram_type": "agent_loop"
        },
        "code_example": {
            "title": "Simulating a Minimal ReAct Agent Loop in Python",
            "language": "python",
            "code": "def mock_calculator_tool(expression: str) -> str:\n    try:\n        return str(eval(expression))\n    except Exception as e:\n        return f\"Error: {e}\"\n\n# Simulated agent trace\ntrace = [\n    {\"type\": \"Thought\", \"content\": \"The user wants to know 145 * 38. I will invoke the calculator tool.\"},\n    {\"type\": \"Action\", \"tool\": \"calculator\", \"args\": \"145 * 38\"},\n    {\"type\": \"Observation\", \"result\": mock_calculator_tool(\"145 * 38\")},\n    {\"type\": \"Thought\", \"content\": \"The tool returned 5510. I can now answer the user directly.\"},\n    {\"type\": \"Final Answer\", \"content\": \"145 multiplied by 38 equals 5,510.\"}\n]\n\nfor step in trace:\n    print(f\"[{step['type']}]: {step.get('content') or step.get('args') or step.get('result')}\")",
            "explanation": "Simulates the Thought -> Action -> Observation -> Response cycle of autonomous AI agents.",
            "output_preview": "[Thought]: The user wants to know 145 * 38. I will invoke the calculator tool.\n[Action]: 145 * 38\n[Observation]: 5510\n[Thought]: The tool returned 5510. I can now answer the user directly.\n[Final Answer]: 145 multiplied by 38 equals 5,510."
        },
        "quiz_id": "quiz-prompt-ai-agents-tool-use",
        "summary": "You learned how AI agents use function calling and the ReAct loop to interact with tools and execute multi-step workflows.",
        "next_lesson_slug": None,
        "prev_lesson_slug": "prompt-chain-of-thought-reasoning"
    }
]

QUIZZES_DATA = [
    # Course 1 Quizzes
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
        "id": "quiz-py-data-structures-comprehensions",
        "lesson_slug": "py-data-structures-comprehensions",
        "title": "Python Data Structures & Comprehensions Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "What is the output of the list comprehension: `[x**2 for x in [1, 2, 3, 4] if x % 2 == 0]`?",
                "options": ["[1, 9]", "[4, 16]", "[1, 4, 9, 16]", "[2, 4]"],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "python_basics",
                "explanation": "The condition `if x % 2 == 0` filters only even numbers (2 and 4). The expression `x**2` squares them, producing [4, 16].",
                "hint": "Filter even numbers first, then square each."
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
                "explanation": "Broadcasting aligns trailing (rightmost) dimensions. For `(4, 3)` and `(4,)`, the trailing dimensions are `3` and `4`. Since neither is equal nor 1, NumPy raises a ValueError.",
                "hint": "Compare trailing dimensions from right to left. They must be equal or one of them must be 1."
            }
        ]
    },
    {
        "id": "quiz-py-numpy-matrix-operations",
        "lesson_slug": "py-numpy-matrix-operations",
        "title": "NumPy Matrix Operations Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "If matrix A has shape (5, 8) and matrix B has shape (8, 3), what is the shape of the matrix product A @ B?",
                "options": ["(5, 3)", "(8, 8)", "(5, 8)", "(8, 3)"],
                "correct_answer": 0,
                "points": 10,
                "skill_tag": "numpy_basics",
                "explanation": "In matrix multiplication (M, K) @ (K, N), the inner dimension K=8 matches and cancels, leaving shape (M, N) = (5, 3).",
                "hint": "Outer dimensions define the resulting output shape."
            }
        ]
    },
    {
        "id": "quiz-py-pandas-dataframes-cleaning",
        "lesson_slug": "py-pandas-dataframes-cleaning",
        "title": "Pandas Data Cleaning & Preprocessing Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "Why is it usually preferable to impute missing numeric values with the column median rather than the column mean?",
                "options": [
                    "Median takes less memory to store",
                    "Median is robust to extreme outliers and skewed data distributions",
                    "Mean is only defined for integer values",
                    "Pandas cannot compute the mean of a column"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "data_preprocessing",
                "explanation": "The median represents the exact 50th percentile and is not pulled by massive outliers (like a $10M salary entry), making it safer for real-world imputation.",
                "hint": "Think about how one billionaire skews the average income of a small town."
            }
        ]
    },

    # Course 2 Quizzes
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
                "explanation": "When the dot product between two non-zero vectors is 0, cos(theta) = 0, meaning the angle between them is 90 degrees (orthogonal / independent).",
                "hint": "Recall that a dot product of 0 means 90 degree angle."
            }
        ]
    },
    {
        "id": "quiz-math-matrix-multiplication",
        "lesson_slug": "math-matrix-multiplication",
        "title": "Matrix Multiplication & Transformations Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "What is the primary geometric effect of multiplying a 2D data vector by a 2x2 identity matrix [[1, 0], [0, 1]]?",
                "options": [
                    "The vector is rotated 180 degrees",
                    "The vector remains completely unchanged in position and length",
                    "The vector's coordinates are doubled",
                    "The vector collapses to the origin (0, 0)"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "linear_algebra",
                "explanation": "The identity matrix is the matrix equivalent of the number 1. Multiplying any vector by the identity matrix leaves it unchanged.",
                "hint": "Identity matrix acts like multiplying by 1."
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
        "id": "quiz-math-chain-rule-backprop-math",
        "lesson_slug": "math-chain-rule-backprop-math",
        "title": "The Chain Rule Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "If y = g(u) and u = h(x), what is the Chain Rule formula for dy/dx?",
                "options": [
                    "(dy/du) + (du/dx)",
                    "(dy/du) * (du/dx)",
                    "(dy/du) / (du/dx)",
                    "dy - dx"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "calculus",
                "explanation": "The Chain Rule states that the derivative of a composite function is the product of the intermediate derivatives: dy/dx = (dy/du) * (du/dx).",
                "hint": "Think of multiplying connected gears."
            }
        ]
    },
    {
        "id": "quiz-math-probability-bayes-theorem",
        "lesson_slug": "math-probability-bayes-theorem",
        "title": "Probability & Bayes' Theorem Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "In Bayes' Theorem P(A|B) = [P(B|A) * P(A)] / P(B), what is P(A) called?",
                "options": [
                    "The Likelihood",
                    "The Prior Probability (initial baseline belief before observing evidence B)",
                    "The Posterior Probability",
                    "The Marginal Variance"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "probability",
                "explanation": "P(A) is the Prior Probability—our existing belief about A before any new evidence B is observed.",
                "hint": "It comes *prior* to observing new clues."
            }
        ]
    },

    # Course 3 Quizzes
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
        "id": "quiz-ml-gradient-descent-intuition",
        "lesson_slug": "ml-gradient-descent-intuition",
        "title": "Gradient Descent Mechanics Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "What happens when training a neural network with an excessively large learning rate (e.g. alpha = 100.0)?",
                "options": [
                    "The model learns instantaneously on step 1",
                    "The parameters overshoot the valley floor and loss diverges to infinity / NaN",
                    "The model parameters freeze and make zero progress",
                    "Memory usage doubles"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "optimization",
                "explanation": "An excessively large learning rate causes huge leaps that bounce out of the loss valley, causing numerical overflow and divergent loss.",
                "hint": "Think of jumping so hard you fly off the mountain."
            }
        ]
    },
    {
        "id": "quiz-ml-logistic-regression-classification",
        "lesson_slug": "ml-logistic-regression-classification",
        "title": "Logistic Regression & Sigmoid Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "What is the output range of the standard Sigmoid activation function sigma(z)?",
                "options": [
                    "[-1.0, 1.0]",
                    "(0.0, 1.0) strictly between 0 and 1",
                    "[0.0, infinity)",
                    "(-infinity, +infinity)"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "classification",
                "explanation": "Sigmoid squashes any real number from negative to positive infinity into a strict probability interval (0.0, 1.0).",
                "hint": "Probabilities must always be between 0% and 100%."
            }
        ]
    },
    {
        "id": "quiz-ml-decision-trees-entropy",
        "lesson_slug": "ml-decision-trees-entropy",
        "title": "Decision Trees & Entropy Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "If a subset of data at a tree leaf contains 100 samples and all 100 belong to the 'Spam' class, what is the Shannon Entropy of this node?",
                "options": ["1.0", "0.0 (Completely Pure)", "0.5", "100.0"],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "decision_trees",
                "explanation": "When all items belong to a single class, there is zero uncertainty or disorder. Entropy is 0.0.",
                "hint": "Pure sets have zero disorder."
            }
        ]
    },
    {
        "id": "quiz-ml-kmeans-clustering-algorithm",
        "lesson_slug": "ml-kmeans-clustering-algorithm",
        "title": "K-Means Clustering Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "Is K-Means an example of Supervised or Unsupervised learning?",
                "options": [
                    "Supervised (requires target labels y)",
                    "Unsupervised (finds clusters in unlabeled data X)",
                    "Reinforcement Learning",
                    "Rule-based Expert System"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "clustering",
                "explanation": "K-Means is an unsupervised algorithm because it groups raw data points based on geometric distance without requiring pre-existing ground truth labels.",
                "hint": "Clustering discovers patterns on its own without teacher labels."
            }
        ]
    },

    # Course 4 Quizzes
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
        "id": "quiz-dl-activation-functions",
        "lesson_slug": "dl-activation-functions",
        "title": "Activation Functions Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "What is the output of ReLU(z) when z = -4.5?",
                "options": ["-4.5", "0.0", "4.5", "1.0"],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "neural_networks",
                "explanation": "ReLU(z) = max(0, z). For any negative number, ReLU outputs 0.0.",
                "hint": "ReLU zeroes out all negative numbers."
            }
        ]
    },
    {
        "id": "quiz-dl-backpropagation-calculus",
        "lesson_slug": "dl-backpropagation-calculus",
        "title": "Backpropagation Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "During neural network training, in what order do information and gradients travel?",
                "options": [
                    "Inputs travel forward to produce loss; error gradients travel backwards to update weights",
                    "Gradients travel forward; inputs travel backwards",
                    "Both travel forward simultaneously",
                    "Weights update before the forward pass executes"
                ],
                "correct_answer": 0,
                "points": 10,
                "skill_tag": "backpropagation",
                "explanation": "Inputs pass forward through layers to compute the output prediction and loss. The backward pass then propagates gradients from loss back through weights.",
                "hint": "Think of forward prediction followed by backward feedback."
            }
        ]
    },
    {
        "id": "quiz-dl-cnn-convolution-pooling",
        "lesson_slug": "dl-cnn-convolution-pooling",
        "title": "Convolutional Neural Networks (CNNs) Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "What is the primary function of Max Pooling layers in a CNN?",
                "options": [
                    "To add more color channels to the image",
                    "To reduce spatial dimensions (downsampling) while preserving the most prominent features",
                    "To generate new images",
                    "To compute cross-entropy loss"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "computer_vision",
                "explanation": "Max Pooling downsamples feature maps by picking the highest activation in each small window, reducing computational load and providing spatial shift invariance.",
                "hint": "Max pooling shrinks the size while keeping the highest values."
            }
        ]
    },

    # Course 5 Quizzes
    {
        "id": "quiz-genai-tokenization-embeddings",
        "lesson_slug": "genai-tokenization-embeddings",
        "title": "Tokenization & Embeddings Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "What is an embedding vector in modern Natural Language Processing?",
                "options": [
                    "A file path on the hard drive",
                    "A dense list of floating-point numbers where geometric proximity represents semantic meaning",
                    "A single binary true/false flag",
                    "An encrypted password hash"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "nlp_embeddings",
                "explanation": "An embedding maps words, sentences, or images into a continuous multidimensional vector space where similar concepts cluster together geometrically.",
                "hint": "Think of coordinates on a high-dimensional concept map."
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
    },
    {
        "id": "quiz-genai-rag-architecture-pipeline",
        "lesson_slug": "genai-rag-architecture-pipeline",
        "title": "RAG Architecture Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "What is the primary benefit of Retrieval-Augmented Generation (RAG) over relying solely on a model's pre-trained weights?",
                "options": [
                    "RAG makes the model run without using any electricity",
                    "RAG grounds the model in up-to-date, verifiable external documents to reduce hallucinations",
                    "RAG translates all text to Latin",
                    "RAG removes the need for tokenizers"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "rag_systems",
                "explanation": "RAG injects relevant text snippets from private databases directly into the prompt, giving the model current factual context and eliminating hallucinations.",
                "hint": "Think of an open-book exam where the model can read exact reference excerpts."
            }
        ]
    },

    # Course 6 Quizzes
    {
        "id": "quiz-prompt-foundations-few-shot",
        "lesson_slug": "prompt-foundations-few-shot",
        "title": "Prompt Foundations & Few-Shot Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "What is Few-Shot Prompting?",
                "options": [
                    "Running the model only a few times a day to save API costs",
                    "Providing 2-3 input and expected output examples inside the prompt to demonstrate the target format",
                    "Limiting the model's vocabulary to 100 words",
                    "Fine-tuning model weights with backpropagation"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "prompt_engineering",
                "explanation": "Few-shot prompting provides concrete examples of the task directly in the prompt context, guiding the model's format and style without updating model weights.",
                "hint": "Think of showing examples before asking the student to solve a problem."
            }
        ]
    },
    {
        "id": "quiz-prompt-chain-of-thought-reasoning",
        "lesson_slug": "prompt-chain-of-thought-reasoning",
        "title": "Chain-of-Thought Reasoning Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "Why does adding 'Think step-by-step before answering' improve LLM accuracy on complex reasoning tasks?",
                "options": [
                    "It doubles the computer's CPU clock speed",
                    "It forces the model to generate intermediate reasoning tokens that act as a working memory scratchpad",
                    "It automatically searches Google in the background",
                    "It bypasses all safety filters"
                ],
                "correct_answer": 1,
                "points": 10,
                "skill_tag": "prompt_engineering",
                "explanation": "LLMs predict token by token. Generating intermediate reasoning steps gives the model computational tokens to work out math and logic before emitting the final conclusion.",
                "hint": "It provides a scratchpad for step-by-step thinking."
            }
        ]
    },
    {
        "id": "quiz-prompt-ai-agents-tool-use",
        "lesson_slug": "prompt-ai-agents-tool-use",
        "title": "AI Autonomous Agents & ReAct Quiz",
        "passing_score": 70,
        "questions": [
            {
                "id": "q1",
                "type": "multiple_choice",
                "question": "What are the core steps of the ReAct (Reason + Act) agent loop?",
                "options": [
                    "Thought -> Action (Tool Call) -> Observation (Tool Output) -> Repeat / Answer",
                    "Compile -> Link -> Execute -> Crash",
                    "Download -> Extract -> Install -> Reboot",
                    "Prompt -> Output -> Exit"
                ],
                "correct_answer": 0,
                "points": 10,
                "skill_tag": "ai_agents",
                "explanation": "ReAct stands for Reason + Act: The agent reasons about its current state, calls an external tool, observes the result, and loops until the goal is achieved.",
                "hint": "Reason, Act, Observe, Repeat."
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
        "matching_lessons": ["py-intro-variables", "py-data-structures-comprehensions", "py-numpy-arrays-broadcasting", "py-numpy-matrix-operations"]
    },
    {
        "id": "skill-data-preprocessing",
        "name": "Data Preprocessing & Pandas",
        "category": "Data Science",
        "description": "Tabular manipulation, missing value imputation, and feature engineering.",
        "icon": "Database",
        "tier": 1,
        "prerequisites": ["skill-python-basics"],
        "mastery_threshold": 70,
        "matching_lessons": ["py-pandas-dataframes-cleaning"]
    },
    {
        "id": "skill-linear-algebra",
        "name": "Linear Algebra & Vectors",
        "category": "Mathematics",
        "description": "Vector dot products, geometric cosine similarity, and matrix transformations.",
        "icon": "Binary",
        "tier": 1,
        "prerequisites": ["skill-python-basics"],
        "mastery_threshold": 70,
        "matching_lessons": ["math-vectors-dot-products", "math-matrix-multiplication"]
    },
    {
        "id": "skill-calculus",
        "name": "Calculus & Optimization",
        "category": "Mathematics",
        "description": "Derivatives, partial slopes, gradient vectors, and the Chain Rule.",
        "icon": "TrendingUp",
        "tier": 2,
        "prerequisites": ["skill-linear-algebra"],
        "mastery_threshold": 70,
        "matching_lessons": ["math-derivatives-gradients", "math-chain-rule-backprop-math"]
    },
    {
        "id": "skill-probability",
        "name": "Probability & Bayes",
        "category": "Mathematics",
        "description": "Bayes Theorem, prior/posterior probabilities, and likelihood estimation.",
        "icon": "Dice5",
        "tier": 2,
        "prerequisites": ["skill-linear-algebra"],
        "mastery_threshold": 70,
        "matching_lessons": ["math-probability-bayes-theorem"]
    },
    {
        "id": "skill-regression",
        "name": "Classical Machine Learning",
        "category": "Machine Learning",
        "description": "Linear regression, loss surfaces, MSE, and gradient descent optimization.",
        "icon": "Cpu",
        "tier": 2,
        "prerequisites": ["skill-calculus"],
        "mastery_threshold": 70,
        "matching_lessons": ["ml-linear-regression-ols", "ml-gradient-descent-intuition"]
    },
    {
        "id": "skill-classification",
        "name": "Classification & Trees",
        "category": "Machine Learning",
        "description": "Logistic regression, Sigmoid curves, Decision Trees, and Entropy.",
        "icon": "GitFork",
        "tier": 2,
        "prerequisites": ["skill-regression"],
        "mastery_threshold": 70,
        "matching_lessons": ["ml-logistic-regression-classification", "ml-decision-trees-entropy", "ml-kmeans-clustering-algorithm"]
    },
    {
        "id": "skill-neural-networks",
        "name": "Deep Neural Networks",
        "category": "Deep Learning",
        "description": "Multi-layer perceptron forward prop, ReLU activations, and Backpropagation.",
        "icon": "Network",
        "tier": 3,
        "prerequisites": ["skill-regression"],
        "mastery_threshold": 70,
        "matching_lessons": ["dl-perceptron-forward-prop", "dl-activation-functions", "dl-backpropagation-calculus"]
    },
    {
        "id": "skill-computer-vision",
        "name": "Computer Vision & CNNs",
        "category": "Deep Learning",
        "description": "2D convolution filters, feature map hierarchies, and Max Pooling.",
        "icon": "Eye",
        "tier": 3,
        "prerequisites": ["skill-neural-networks"],
        "mastery_threshold": 70,
        "matching_lessons": ["dl-cnn-convolution-pooling"]
    },
    {
        "id": "skill-transformers",
        "name": "Transformers & Generative AI",
        "category": "Generative AI",
        "description": "Query/Key/Value self-attention, token contextualization, and RAG pipelines.",
        "icon": "Sparkles",
        "tier": 4,
        "prerequisites": ["skill-neural-networks"],
        "mastery_threshold": 70,
        "matching_lessons": ["genai-tokenization-embeddings", "genai-self-attention-transformers", "genai-rag-architecture-pipeline"]
    },
    {
        "id": "skill-prompt-engineering",
        "name": "Prompt Engineering & Agents",
        "category": "Practical AI",
        "description": "Few-shot prompting, Chain of Thought, tool usage, and autonomous ReAct agents.",
        "icon": "Bot",
        "tier": 4,
        "prerequisites": ["skill-python-basics"],
        "mastery_threshold": 70,
        "matching_lessons": ["prompt-foundations-few-shot", "prompt-chain-of-thought-reasoning", "prompt-ai-agents-tool-use"]
    }
]
