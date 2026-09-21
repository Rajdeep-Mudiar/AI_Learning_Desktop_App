"""
AI / ML Track Seed Data
Levels 1 - 8 covering:
- Level 1: Mathematics (Linear Algebra, Calculus, Probability & Statistics)
- Level 2: Python Data Computing Stack (NumPy, Pandas, Scikit-learn)
- Level 3: Classical Machine Learning Algorithms & Optimization
- Level 4: Deep Learning Foundations & PyTorch Computation Graphs
- Level 5: Computer Vision (CNNs, YOLO, U-Net, Vision Transformers)
- Level 6: Natural Language Processing & Transformers
- Level 7: Generative AI, RAG & Autonomous Agent Frameworks
- Level 8: Production MLOps, Quantization & Model Serving
"""

COURSES_DATA = [
    {
        "id": "course-aiml-lvl1",
        "title": "AI/ML Level 1: Mathematical Foundations for Machine Learning",
        "slug": "aiml-level-1-mathematics",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "description": "Linear Algebra (Vectors, Matrices, Eigenvalues, SVD), Multivariable Calculus (Gradients, Chain Rule), Probability (Bayes Theorem), and Statistics.",
        "category": "Mathematics",
        "level": "beginner",
        "estimated_hours": 16,
        "thumbnail_url": "/assets/courses/aiml-math.png",
        "modules": [
            {
                "id": "mod-aiml-1-1",
                "title": "Module 1: Linear Algebra & Matrix Calculus",
                "description": "Vector projections, Matrix multiplication complexity, Eigenvalue decomposition, and SVD.",
                "order": 1,
                "lesson_ids": ["aiml-linear-algebra-eigen-svd", "aiml-multivariable-calculus-gradients"]
            },
            {
                "id": "mod-aiml-1-2",
                "title": "Module 2: Probability Distributions & Inferential Statistics",
                "description": "Bayesian probability, Gaussian distributions, Expectation, and Hypothesis testing.",
                "order": 2,
                "lesson_ids": ["aiml-probability-bayes-distributions", "aiml-statistics-hypothesis-testing"]
            }
        ]
    },
    {
        "id": "course-aiml-lvl2",
        "title": "AI/ML Level 2: Python Data Computing Stack & Feature Pipelines",
        "slug": "aiml-level-2-data-stack",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "description": "Master vectorized NumPy matrix operations, Pandas DataFrame transformations, and Scikit-learn preprocessing pipelines.",
        "category": "Programming Foundations",
        "level": "beginner",
        "estimated_hours": 14,
        "thumbnail_url": "/assets/courses/aiml-stack.png",
        "modules": [
            {
                "id": "mod-aiml-2-1",
                "title": "Module 1: Vectorized NumPy & Data Cleaning Pipelines",
                "description": "Broadcasting rules, SIMD array strides, missing value imputation, and one-hot encoding.",
                "order": 1,
                "lesson_ids": ["aiml-numpy-vectorization-broadcasting", "aiml-pandas-feature-engineering-pipeline"]
            }
        ]
    },
    {
        "id": "course-aiml-lvl3",
        "title": "AI/ML Level 3: Classical Machine Learning & Tree Ensembles",
        "slug": "aiml-level-3-classical-ml",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "description": "Supervised (Linear/Logistic Regression, Decision Trees, Random Forest, XGBoost, SVM) & Unsupervised (K-Means, PCA, DBSCAN) learning.",
        "category": "Machine Learning",
        "level": "intermediate",
        "estimated_hours": 18,
        "thumbnail_url": "/assets/courses/aiml-classical.png",
        "modules": [
            {
                "id": "mod-aiml-3-1",
                "title": "Module 1: Supervised Regression & Classification",
                "description": "Ordinary Least Squares Normal Equation, Logistic loss, and Support Vector hyperplanes.",
                "order": 1,
                "lesson_ids": ["aiml-regression-logistic-svm", "aiml-random-forest-xgboost-ensembles"]
            },
            {
                "id": "mod-aiml-3-2",
                "title": "Module 2: Dimensionality Reduction & Clustering",
                "description": "PCA variance maximization, K-Means++ clustering, and cross-validation metrics.",
                "order": 2,
                "lesson_ids": ["aiml-pca-kmeans-unsupervised", "aiml-model-evaluation-bias-variance"]
            }
        ]
    },
    {
        "id": "course-aiml-lvl4",
        "title": "AI/ML Level 4: Deep Learning Foundations & PyTorch Tensors",
        "slug": "aiml-level-4-deep-learning",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "description": "Neural Networks, Autograd computational graphs, Backpropagation, Optimizers (Adam, SGD), BatchNorm, and Dropout in PyTorch.",
        "category": "Deep Learning",
        "level": "advanced",
        "estimated_hours": 20,
        "thumbnail_url": "/assets/courses/aiml-deep-learning.png",
        "modules": [
            {
                "id": "mod-aiml-4-1",
                "title": "Module 1: Neural Network Architecture & Backpropagation",
                "description": "Multivariate chain rule gradient flow, vanishing gradient solutions, and PyTorch training loops.",
                "order": 1,
                "lesson_ids": ["aiml-backpropagation-gradient-flow", "aiml-pytorch-training-loop-optimizers"]
            }
        ]
    },
    {
        "id": "course-aiml-lvl5",
        "title": "AI/ML Level 5: Computer Vision & Object Detection (YOLO, ViT)",
        "slug": "aiml-level-5-computer-vision",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "description": "Convolutional Neural Networks, 2D kernels, ResNet residual blocks, YOLO object detection, and Vision Transformers.",
        "category": "Deep Learning",
        "level": "advanced",
        "estimated_hours": 22,
        "thumbnail_url": "/assets/courses/aiml-cv.png",
        "modules": [
            {
                "id": "mod-aiml-5-1",
                "title": "Module 1: CNNs, ResNet & Real-Time YOLO Detection",
                "description": "Spatial convolution, receptive fields, residual skip connections, and anchor-free object detection.",
                "order": 1,
                "lesson_ids": ["aiml-cnn-resnet-architectures", "aiml-yolo-object-detection-segmentation"]
            }
        ]
    },
    {
        "id": "course-aiml-lvl6",
        "title": "AI/ML Level 6: Natural Language Processing & Transformers",
        "slug": "aiml-level-6-nlp-transformers",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "description": "Tokenization, Word2Vec, Scaled Dot-Product Attention, Multi-Head Attention, Transformer Encoders/Decoders (BERT, GPT, T5).",
        "category": "Deep Learning",
        "level": "advanced",
        "estimated_hours": 24,
        "thumbnail_url": "/assets/courses/aiml-nlp.png",
        "modules": [
            {
                "id": "mod-aiml-6-1",
                "title": "Module 1: Self-Attention & The Transformer Architecture",
                "description": "Scaled dot-product attention formula, positional encoding, and encoder-decoder stacks.",
                "order": 1,
                "lesson_ids": ["aiml-scaled-dot-product-attention", "aiml-bert-gpt-transformer-stacks"]
            }
        ]
    },
    {
        "id": "course-aiml-lvl7",
        "title": "AI/ML Level 7: Generative AI, RAG & Autonomous Agents",
        "slug": "aiml-level-7-genai-rag-agents",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "description": "Vector databases (Chroma/Pinecone), Retrieval-Augmented Generation (RAG), Fine-tuning with LoRA/QLoRA, and LangGraph multi-agent systems.",
        "category": "Generative AI",
        "level": "expert",
        "estimated_hours": 26,
        "thumbnail_url": "/assets/courses/aiml-genai.png",
        "modules": [
            {
                "id": "mod-aiml-7-1",
                "title": "Module 1: Production RAG Pipelines & Parameter-Efficient Fine-Tuning",
                "description": "Chunking, embedding similarity, cross-encoders, LoRA adapter weights, and LangGraph loops.",
                "order": 1,
                "lesson_ids": ["aiml-rag-vector-databases-retrieval", "aiml-lora-qlora-agentic-workflows"]
            }
        ]
    },
    {
        "id": "course-aiml-lvl8",
        "title": "AI/ML Level 8: Production MLOps, Quantization & Serving",
        "slug": "aiml-level-8-mlops-serving",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "description": "Post-training quantization (AWQ/GGUF), ONNX Runtime, TensorRT-LLM, MLflow experiment tracking, and FastAPI microservices.",
        "category": "Practical AI",
        "level": "expert",
        "estimated_hours": 22,
        "thumbnail_url": "/assets/courses/aiml-mlops.png",
        "modules": [
            {
                "id": "mod-aiml-8-1",
                "title": "Module 1: Quantization & High-Throughput Serving",
                "description": "FP16/INT8/INT4 weight quantization, vLLM continuous batching, and Docker container deployments.",
                "order": 1,
                "lesson_ids": ["aiml-quantization-onnx-tensorrt", "aiml-mlops-mlflow-serving-docker"]
            }
        ]
    }
]

LESSONS_DATA = [
    {
        "id": "aiml-linear-algebra-eigen-svd",
        "title": "Linear Algebra: Vector Spaces, Eigenvalues & SVD",
        "slug": "aiml-linear-algebra-eigen-svd",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl1",
        "order": 1,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Linear Algebra Foundations for Machine Learning

### 1. Matrix Transformations & Eigenvectors
An eigenvector $v$ of a square matrix $A$ satisfies $A v = \\lambda v$, where $\\lambda$ is the corresponding eigenvalue.

### 2. Singular Value Decomposition (SVD)
Every matrix $A \\in \\mathbb{R}^{M \\times N}$ can be factored as:
$$A = U \\Sigma V^T$$
Where $U \\in \\mathbb{R}^{M \\times M}$ and $V \\in \\mathbb{R}^{N \\times N}$ are orthogonal matrices, and $\\Sigma$ contains singular values $\\sigma_1 \\ge \\sigma_2 \\ge \\dots \\ge 0$.
"""
    },
    {
        "id": "aiml-multivariable-calculus-gradients",
        "title": "Multivariable Calculus: Gradients, Jacobians & Hessians",
        "slug": "aiml-multivariable-calculus-gradients",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl1",
        "order": 2,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Matrix Calculus & Gradient Descent

The gradient vector $\\nabla_x f(x)$ points in the direction of steepest ascent:
$$x^{(t+1)} = x^{(t)} - \\eta \\nabla_x f(x^{(t)})$$
"""
    },
    {
        "id": "aiml-probability-bayes-distributions",
        "title": "Probability Theory: Bayes Theorem & Maximum Likelihood",
        "slug": "aiml-probability-bayes-distributions",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl1",
        "order": 3,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Bayes Theorem & Maximum Likelihood Estimation (MLE)

$$P(\\theta | D) = \\frac{P(D | \\theta) P(\\theta)}{P(D)} = \\frac{\\text{Likelihood} \\times \\text{Prior}}{\\text{Evidence}}$$
"""
    },
    {
        "id": "aiml-statistics-hypothesis-testing",
        "title": "Inferential Statistics: p-values & Confidence Intervals",
        "slug": "aiml-statistics-hypothesis-testing",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl1",
        "order": 4,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Hypothesis Testing & A/B Testing Metrics

Evaluating null hypothesis $H_0$ vs alternative hypothesis $H_1$ using two-sample t-tests and statistical power.
"""
    },
    {
        "id": "aiml-numpy-vectorization-broadcasting",
        "title": "NumPy Vectorization, Strides & SIMD Broadcasting",
        "slug": "aiml-numpy-vectorization-broadcasting",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl2",
        "order": 1,
        "xp_reward": 65,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Vectorized Array Computing

NumPy avoids Python interpreter overhead by executing array operations in C with contiguous C-strides and SIMD CPU instructions.
"""
    },
    {
        "id": "aiml-pandas-feature-engineering-pipeline",
        "title": "Pandas DataFrames & Scikit-learn Pipeline Transformers",
        "slug": "aiml-pandas-feature-engineering-pipeline",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl2",
        "order": 2,
        "xp_reward": 65,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Feature Preprocessing Pipelines

Building reusable `ColumnTransformer` pipelines combining `StandardScaler`, `OneHotEncoder`, and `SimpleImputer` to prevent data leakage during cross-validation.
"""
    },
    {
        "id": "aiml-regression-logistic-svm",
        "title": "OLS Linear Regression, Logistic Loss & Support Vector Machines",
        "slug": "aiml-regression-logistic-svm",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl3",
        "order": 1,
        "xp_reward": 70,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Linear Models & Maximum Margin SVM

### Normal Equation:
$$\\theta = (X^T X)^{-1} X^T y$$

### SVM Soft-Margin Optimization:
$$\\min_{w, b, \\xi} \\frac{1}{2} \\|w\\|^2 + C \\sum_{i=1}^N \\xi_i \\quad \\text{s.t. } y_i (w^T x_i + b) \\ge 1 - \\xi_i$$
"""
    },
    {
        "id": "aiml-random-forest-xgboost-ensembles",
        "title": "Random Forests & Gradient Boosted Trees (XGBoost)",
        "slug": "aiml-random-forest-xgboost-ensembles",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl3",
        "order": 2,
        "xp_reward": 75,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Bagging vs Boosting

- **Random Forest (Bagging)**: Reduces **variance** by averaging independent bootstrap decision trees.
- **Gradient Boosting (XGBoost)**: Reduces **bias** by sequentially fitting new trees to the pseudo-residuals of preceding models.
"""
    },
    {
        "id": "aiml-pca-kmeans-unsupervised",
        "title": "Principal Component Analysis (PCA) & K-Means++",
        "slug": "aiml-pca-kmeans-unsupervised",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl3",
        "order": 3,
        "xp_reward": 70,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Unsupervised Learning: PCA & K-Means

PCA projects data onto eigenvectors of the covariance matrix $\\Sigma = \\frac{1}{N} X^T X$ corresponding to the largest eigenvalues.
"""
    },
    {
        "id": "aiml-model-evaluation-bias-variance",
        "title": "Bias-Variance Tradeoff, Cross-Validation & ROC-AUC",
        "slug": "aiml-model-evaluation-bias-variance",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl3",
        "order": 4,
        "xp_reward": 70,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Generalization Error & Metrics

$$\\text{Total Error} = \\text{Bias}^2 + \\text{Variance} + \\text{Irreducible Noise}$$
"""
    },
    {
        "id": "aiml-backpropagation-gradient-flow",
        "title": "Multilayer Perceptrons & Backpropagation Gradient Flow",
        "slug": "aiml-backpropagation-gradient-flow",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl4",
        "order": 1,
        "xp_reward": 80,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Reverse-Mode Automatic Differentiation

Computing parameter updates via multivariate chain rule:
$$\\frac{\\partial L}{\\partial W^{(l)}} = \\delta^{(l)} \\cdot (a^{(l-1)})^T$$
"""
    },
    {
        "id": "aiml-pytorch-training-loop-optimizers",
        "title": "PyTorch: Adam Optimizer, BatchNorm & Learning Schedules",
        "slug": "aiml-pytorch-training-loop-optimizers",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl4",
        "order": 2,
        "xp_reward": 80,
        "visual_diagram_type": "two_pointers_array",
        "content": """# PyTorch Production Training Loops

```python
import torch
import torch.nn as nn

optimizer.zero_grad()
outputs = model(inputs)
loss = criterion(outputs, targets)
loss.backward()
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
optimizer.step()
```
"""
    },
    {
        "id": "aiml-cnn-resnet-architectures",
        "title": "Convolutional Networks & ResNet Residual Connections",
        "slug": "aiml-cnn-resnet-architectures",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl5",
        "order": 1,
        "xp_reward": 85,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Residual Networks (ResNet)

Residual block computes $\\mathcal{F}(x) + x$, allowing gradient signals $\\frac{\\partial L}{\\partial x} = \\frac{\\partial L}{\\partial y} \\left(\\frac{\\partial \\mathcal{F}}{\\partial x} + 1\\right)$ to flow directly to early layers without vanishing.
"""
    },
    {
        "id": "aiml-yolo-object-detection-segmentation",
        "title": "YOLO Object Detection & U-Net Semantic Segmentation",
        "slug": "aiml-yolo-object-detection-segmentation",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl5",
        "order": 2,
        "xp_reward": 85,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Real-Time Object Detection (YOLO)

Single-stage bounding box prediction, Intersection over Union (IoU) loss, and Non-Maximum Suppression (NMS).
"""
    },
    {
        "id": "aiml-scaled-dot-product-attention",
        "title": "Attention Is All You Need: Scaled Dot-Product & MHA",
        "slug": "aiml-scaled-dot-product-attention",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl6",
        "order": 1,
        "xp_reward": 90,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Scaled Dot-Product Attention Formula

$$\\text{Attention}(Q, K, V) = \\text{Softmax}\\left(\\frac{Q K^T}{\\sqrt{d_k}}\\right) V$$
Dividing by $\\sqrt{d_k}$ stabilizes the variance of the dot product to 1.0, preventing softmax saturation into vanishing gradient regions.
"""
    },
    {
        "id": "aiml-bert-gpt-transformer-stacks",
        "title": "Transformer Encoders (BERT) & Decoders (GPT / Llama)",
        "slug": "aiml-bert-gpt-transformer-stacks",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl6",
        "order": 2,
        "xp_reward": 90,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Autoregressive Decoder LLMs vs Bidirectional Encoders

- **BERT (Encoder)**: Bidirectional masked language modeling.
- **GPT / Llama (Decoder)**: Causal autoregressive next-token prediction with Rotary Positional Embeddings (RoPE).
"""
    },
    {
        "id": "aiml-rag-vector-databases-retrieval",
        "title": "Retrieval-Augmented Generation (RAG) & Vector Search",
        "slug": "aiml-rag-vector-databases-retrieval",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl7",
        "order": 1,
        "xp_reward": 95,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Enterprise RAG Architecture

1. Document Parsing & Chunking with overlap
2. Dense vector embedding generation
3. HNSW approximate nearest neighbor search
4. Cross-encoder re-ranking
5. Prompt synthesis with grounding context
"""
    },
    {
        "id": "aiml-lora-qlora-agentic-workflows",
        "title": "LoRA Parameter-Efficient Fine-Tuning & LangGraph Agents",
        "slug": "aiml-lora-qlora-agentic-workflows",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl7",
        "order": 2,
        "xp_reward": 95,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Low-Rank Adaptation (LoRA)

Freezes pretrained weight matrix $W_0 \\in \\mathbb{R}^{d \\times k}$ and injects trainable low-rank rank decomposition matrices $B A$, where $B \\in \\mathbb{R}^{d \\times r}$ and $A \\in \\mathbb{R}^{r \\times k}$ with $r \\ll \\min(d, k)$:
$$W = W_0 + \\frac{\\alpha}{r} B A$$
"""
    },
    {
        "id": "aiml-quantization-onnx-tensorrt",
        "title": "Model Quantization (AWQ, GGUF, INT4) & TensorRT",
        "slug": "aiml-quantization-onnx-tensorrt",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl8",
        "order": 1,
        "xp_reward": 100,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Quantization & Inference Accelerators

Compressing FP32/FP16 models to INT8/INT4 weights reducing VRAM memory footprints by $75\\%$ while preserving perplexity via Activation-aware Weight Quantization (AWQ).
"""
    },
    {
        "id": "aiml-mlops-mlflow-serving-docker",
        "title": "Production MLOps: MLflow, vLLM & Kubernetes Deployments",
        "slug": "aiml-mlops-mlflow-serving-docker",
        "domain": "ai-ml",
        "color": "#6366F1",
        "icon": "Cpu",
        "is_published": True,
        "skills_taught": ['Linear Algebra', 'Machine Learning', 'PyTorch Tensors', 'Transformers', 'RAG'],
        "course_id": "course-aiml-lvl8",
        "order": 2,
        "xp_reward": 100,
        "visual_diagram_type": "two_pointers_array",
        "content": """# End-to-End MLOps Infrastructure

Model registry tracking, PagedAttention continuous batching via vLLM, and autoscaling GPU inference clusters with Prometheus telemetry.
"""
    }
]

QUIZZES_DATA = [
    {
        "id": "quiz-aiml-lvl1",
        "lesson_id": "aiml-linear-algebra-eigen-svd",
        "title": "AI/ML Mathematics & Neural Foundations Diagnostic",
        "passing_score": 80,
        "questions": [
            {
                "id": "q-aiml-1-1",
                "question": "Why does Scaled Dot-Product Attention divide by sqrt(d_k)?",
                "options": [
                    "To convert the matrix into an orthogonal basis",
                    "To normalize dot-product variance back to 1.0 and prevent softmax vanishing gradients",
                    "To compute the inverse matrix",
                    "To drop 50% of the attention connections"
                ],
                "correct_option_index": 1,
                "explanation": "When dimension d_k is large, dot product variance equals d_k. Scaling by sqrt(d_k) keeps the softmax inputs within active gradient regions."
            }
        ]
    }
]

SKILLS_DATA = [
    {
        "id": "skill-aiml-core",
        "name": "AI/ML Mathematics & Machine Learning",
        "category": "Machine Learning",
        "level": 1,
        "unlocked": True,
        "progress": 0.0,
        "prerequisites": [],
        "description": "Master Linear Algebra, Calculus, Classical ML, and Scikit-learn."
    },
    {
        "id": "skill-aiml-deep-genai",
        "name": "Deep Learning & Generative AI",
        "category": "Generative AI",
        "level": 2,
        "unlocked": True,
        "progress": 0.0,
        "prerequisites": ["skill-aiml-core"],
        "description": "Master PyTorch, Transformers, RAG, LoRA, and MLOps."
    }
]
