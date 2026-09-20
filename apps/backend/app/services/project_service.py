from typing import List, Dict, Any, Optional
from app.schemas.project import (
    ProjectTrack,
    ProjectMilestone,
    VivaQuestionResponse,
    VivaEvaluationResponse,
    PortfolioExportResponse
)

PROJECTS_CATALOG: List[ProjectTrack] = [
    ProjectTrack(
        id="spam-classifier",
        title="Real-Time SMS & Email Spam Classifier Pipeline",
        tagline="Production NLP text classification pipeline with TF-IDF vectorization and Multinomial Naive Bayes.",
        difficulty="Beginner",
        estimated_hours=6,
        category="NLP",
        description="Build an end-to-end NLP text filtering microservice capable of distinguishing spam from legitimate messages with sub-5ms inference latency.",
        dataset_name="SMS Spam Collection (5,574 labeled messages)",
        architecture="Raw Text -> Regex Preprocessing -> N-gram TF-IDF Vectorizer -> Multinomial Naive Bayes -> Calibration",
        skills_covered=["Text Normalization", "TF-IDF Vectorization", "Laplace Smoothing", "Precision-Recall Optimization"],
        banner_gradient="linear-gradient(135deg, #6366f1, #38bdf8)",
        milestones=[
            ProjectMilestone(
                id="sc-m1",
                step_number=1,
                title="Exploratory Data Analysis & Text Cleaning",
                description="Load corpus, analyze class imbalance, remove punctuation, strip stopwords, and lower-case tokens.",
                tasks=[
                    "Inspect class distribution ratio (87% Ham vs 13% Spam)",
                    "Write regex tokenizer stripping URLs and punctuation",
                    "Compute top vocabulary frequencies per class"
                ],
                starter_code="import re\nimport pandas as pd\n\ndef clean_text(text: str) -> str:\n    # Strip URLs and non-alphanumeric chars\n    return re.sub(r'[^a-zA-Z0-9\\s]', '', text.lower())\n",
                solution_code="import re\ndef clean_text(text: str) -> str:\n    text = re.sub(r'http\\S+|www\\S+', '', text)\n    text = re.sub(r'[^a-zA-Z0-9\\s]', '', text)\n    return text.lower().strip()\n",
                is_completed=True
            ),
            ProjectMilestone(
                id="sc-m2",
                step_number=2,
                title="TF-IDF Feature Extraction & Vectorization",
                description="Convert cleaned strings into weighted numerical vectors using Term Frequency-Inverse Document Frequency.",
                tasks=[
                    "Implement TF-IDF with sublinear term frequency scaling",
                    "Tune max_features and min_df thresholds",
                    "Extract top 20 most discriminative spam keywords"
                ],
                starter_code="from sklearn.feature_extraction.text import TfidfVectorizer\n\nvectorizer = TfidfVectorizer(max_features=3000, ngram_range=(1, 2))\n",
                solution_code="from sklearn.feature_extraction.text import TfidfVectorizer\nvectorizer = TfidfVectorizer(max_features=3000, ngram_range=(1, 2), stop_words='english')\n",
                is_completed=True
            ),
            ProjectMilestone(
                id="sc-m3",
                step_number=3,
                title="Model Training, Calibration & Evaluation",
                description="Fit MultinomialNB and LogisticRegression models, calibrate decision thresholds, and compute PR-AUC.",
                tasks=[
                    "Train baseline MultinomialNB with Laplace smoothing alpha=1.0",
                    "Evaluate Precision at 99% Recall to avoid filtering legitimate emails",
                    "Generate Confusion Matrix and ROC-AUC curve"
                ],
                starter_code="from sklearn.naive_bayes import MultinomialNB\n\nclf = MultinomialNB(alpha=1.0)\n",
                solution_code="from sklearn.naive_bayes import MultinomialNB\nclf = MultinomialNB(alpha=0.5)\nclf.fit(X_train, y_train)\n",
                is_completed=False
            ),
            ProjectMilestone(
                id="sc-m4",
                step_number=4,
                title="Deployment Pipeline & REST Endpoint",
                description="Serialize fitted pipeline into a lightweight pickle artifact and build an interactive REST scoring handler.",
                tasks=[
                    "Export model and vectorizer artifact",
                    "Benchmark latency on batch of 100 requests (< 5ms)",
                    "Generate automated documentation"
                ],
                starter_code="import joblib\n# Save model pipeline\n",
                solution_code="import joblib\njoblib.dump((vectorizer, clf), 'spam_model.pkl')\n",
                is_completed=False
            )
        ]
    ),
    ProjectTrack(
        id="rag-knowledge-assistant",
        title="Retrieval-Augmented Generation (RAG) Assistant",
        tagline="Production document question-answering assistant with semantic chunking, cosine vector similarity, and local LLM synthesis.",
        difficulty="Intermediate",
        estimated_hours=10,
        category="RAG & LLM",
        description="Construct a domain-specific retrieval-augmented knowledge engine capable of answering technical queries with exact source citations.",
        dataset_name="AI Research Paper Corpus (15 PDFs / Markdown)",
        architecture="PDF/Markdown Parser -> Semantic Chunker -> Vector Embedding Store -> Top-K Cosine Retrieval -> Augmented Prompt -> LLM",
        skills_covered=["Semantic Chunking", "Vector Embeddings", "Cosine Similarity", "Prompt Engineering", "Hallucination Mitigation"],
        banner_gradient="linear-gradient(135deg, #10b981, #06b6d4)",
        milestones=[
            ProjectMilestone(
                id="rag-m1",
                step_number=1,
                title="Document Ingestion & Chunking",
                description="Implement overlapping chunking strategy with semantic sliding windows.",
                tasks=[
                    "Parse markdown and technical documentation",
                    "Implement chunker with chunk_size=500 and overlap=50",
                    "Preserve header hierarchy metadata"
                ],
                starter_code="def chunk_document(text: str, chunk_size=500, overlap=50):\n    # Implement sliding window\n    pass\n",
                solution_code="def chunk_document(text: str, chunk_size=500, overlap=50):\n    tokens = text.split()\n    chunks = []\n    for i in range(0, len(tokens), chunk_size - overlap):\n        chunks.append(' '.join(tokens[i:i+chunk_size]))\n    return chunks\n",
                is_completed=True
            ),
            ProjectMilestone(
                id="rag-m2",
                step_number=2,
                title="Embedding Generation & Vector Store Indexing",
                description="Project document chunks into 384-dimensional dense semantic space and index in memory.",
                tasks=[
                    "Generate embeddings for all document chunks",
                    "Compute normalized vector dot products",
                    "Implement Top-K Cosine Similarity search"
                ],
                starter_code="import numpy as np\n\ndef cosine_similarity(q_vec, doc_matrix):\n    return doc_matrix @ q_vec / (np.linalg.norm(doc_matrix, axis=1) * np.linalg.norm(q_vec))\n",
                solution_code="import numpy as np\ndef cosine_similarity(q_vec, doc_matrix):\n    norm_q = q_vec / (np.linalg.norm(q_vec) + 1e-9)\n    norm_docs = doc_matrix / (np.linalg.norm(doc_matrix, axis=1, keepdims=True) + 1e-9)\n    return norm_docs @ norm_q\n",
                is_completed=False
            ),
            ProjectMilestone(
                id="rag-m3",
                step_number=3,
                title="Augmented Prompt Synthesis & Hallucination Guardrails",
                description="Construct grounded prompts and verify answers with citation verification.",
                tasks=[
                    "Synthesize Context + Question prompt template",
                    "Enforce strict 'Answer only using provided context' rule",
                    "Calculate context relevance score"
                ],
                starter_code="# Prompt template constructor\n",
                solution_code="PROMPT = 'Use ONLY the provided context to answer: \\nContext: {context}\\nQuestion: {query}'\n",
                is_completed=False
            )
        ]
    ),
    ProjectTrack(
        id="cnn-digit-recognizer",
        title="CNN Handwritten Digit & Signature Recognizer",
        tagline="Deep convolutional neural network architecture with PyTorch/NumPy for image feature extraction.",
        difficulty="Intermediate",
        estimated_hours=8,
        category="Computer Vision",
        description="Design and train a spatial convolution pipeline with feature map visualization, dropout regularization, and real-time canvas inference.",
        dataset_name="MNIST & Synthetic Signature Patches",
        architecture="28x28 Grayscale Image -> Conv2D (32, 3x3) -> MaxPool2D -> Conv2D (64, 3x3) -> Dense (128) -> Softmax (10)",
        skills_covered=["Spatial Convolutions", "Pooling Layers", "Cross-Entropy Loss", "Feature Map Extraction", "Dropout Regularization"],
        banner_gradient="linear-gradient(135deg, #f59e0b, #ef4444)",
        milestones=[
            ProjectMilestone(
                id="cnn-m1",
                step_number=1,
                title="Data Normalization & Data Augmentation",
                description="Normalize pixel values to [-1.0, 1.0] and apply rotation/translation transforms.",
                tasks=[
                    "Scale uint8 pixels to float32 standard tensors",
                    "Apply random affine jitter (±10° rotation)",
                    "Split into 80% Train, 10% Validation, 10% Test"
                ],
                starter_code="# Normalize pixel values\n",
                solution_code="def normalize_pixels(img):\n    return (img.astype('float32') / 255.0 - 0.5) * 2.0\n",
                is_completed=True
            ),
            ProjectMilestone(
                id="cnn-m2",
                step_number=2,
                title="Conv2D Architecture & Backpropagation",
                description="Build forward graph with 2 Convolution stages, ReLU activations, and Max Pooling.",
                tasks=[
                    "Configure Conv2D kernel weights and biases",
                    "Compute spatial feature map activations",
                    "Measure classification accuracy on test split (> 98%)"
                ],
                starter_code="# Conv2D definition\n",
                solution_code="# Conv2D forward\n",
                is_completed=False
            )
        ]
    )
]

# Viva Examiner Question Bank
VIVA_QUESTIONS: Dict[str, List[Dict[str, str]]] = {
    "spam-classifier": [
        {
            "id": "viva-sc-1",
            "question": "Why did you choose TF-IDF vectorization over dense pretrained word embeddings (like GloVe or BERT) for this spam classification problem?",
            "focus_area": "Architecture & Engineering Trade-offs",
            "rubric": "Candidate should mention computational speed, low latency (<5ms), explainability of top spam token weights, and domain-specific keywords like 'free', 'winner', 'urgent'."
        },
        {
            "id": "viva-sc-2",
            "question": "How does Laplace smoothing (alpha parameter in Naive Bayes) prevent the zero-probability frequency problem during inference on previously unseen tokens?",
            "focus_area": "Mathematical Foundations",
            "rubric": "Candidate must explain that multiplying P(word|class)=0 would wipe out the entire posterior probability, and Laplace smoothing adds pseudo-counts (+alpha / +alpha*|V|)."
        },
        {
            "id": "viva-sc-3",
            "question": "In a production email filter, is False Positive or False Negative more catastrophic? How did you adjust your classification decision threshold accordingly?",
            "focus_area": "Evaluation & Production Safety",
            "rubric": "Candidate must recognize that False Positives (blocking legitimate email) are far worse than False Negatives (spam slipping to inbox), requiring high precision thresholds (e.g. 0.95)."
        }
    ],
    "rag-knowledge-assistant": [
        {
            "id": "viva-rag-1",
            "question": "What are the trade-offs between choosing a small chunk size (e.g. 100 tokens) versus a large chunk size (e.g. 1000 tokens) in your retrieval pipeline?",
            "focus_area": "Architecture",
            "rubric": "Small chunks offer precise semantic match but lose broader context; large chunks preserve context but dilute vector similarity signals and increase LLM token costs."
        },
        {
            "id": "viva-rag-2",
            "question": "How does Cosine Similarity differ from Euclidean (L2) distance when comparing normalized document embedding vectors?",
            "focus_area": "Math/Optimization",
            "rubric": "For unit-normalized vectors (||v||=1), Euclidean distance squared is directly proportional to 2 - 2*CosineSimilarity. Cosine measures angle irrespective of magnitude."
        }
    ]
}


def get_all_projects() -> List[ProjectTrack]:
    return PROJECTS_CATALOG


def get_project_by_id(project_id: str) -> Optional[ProjectTrack]:
    for p in PROJECTS_CATALOG:
        if p.id == project_id:
            return p
    return None


def get_viva_question(project_id: str, step: int = 1) -> VivaQuestionResponse:
    questions = VIVA_QUESTIONS.get(project_id, VIVA_QUESTIONS["spam-classifier"])
    q_idx = min(step - 1, len(questions) - 1)
    q = questions[q_idx]
    return VivaQuestionResponse(
        question_id=q["id"],
        question=q["question"],
        focus_area=q["focus_area"],
        rubric=q["rubric"]
    )


def evaluate_viva_answer(project_id: str, question_id: str, answer: str) -> VivaEvaluationResponse:
    ans_clean = answer.strip().lower()
    length = len(ans_clean.split())

    if length < 8:
        return VivaEvaluationResponse(
            score=45,
            grade="Needs Revision",
            strengths=["Briefly addressed the prompt"],
            areas_for_improvement=["Provide more technical depth", "Explain mathematical rationale and trade-offs explicitly"],
            examiner_feedback="Your response is too brief for an engineering viva. Elaborate on the underlying mathematics and performance trade-offs."
        )

    # Heuristic scoring based on technical keywords
    technical_keywords = [
        "trade-off", "latency", "precision", "recall", "false positive", "vector",
        "dimension", "laplace", "smoothing", "probability", "gradient", "embedding",
        "matrix", "zero", "frequency", "context", "cosine", "dot product", "production"
    ]
    matched_kw = [kw for kw in technical_keywords if kw in ans_clean]
    score = min(100, 60 + len(matched_kw) * 8 + min(20, length // 4))

    if score >= 85:
        grade = "Distinction"
    elif score >= 70:
        grade = "Merit"
    elif score >= 50:
        grade = "Pass"
    else:
        grade = "Needs Revision"

    strengths = [
        f"Solid understanding of {matched_kw[0]}" if matched_kw else "Clear communication style",
        "Demonstrated awareness of real-world deployment constraints"
    ]
    improvements = [
        "Consider quantifying the memory and latency impact in milliseconds/MB",
        "Connect the choice to alternative baseline models"
    ]

    return VivaEvaluationResponse(
        score=score,
        grade=grade,
        strengths=strengths,
        areas_for_improvement=improvements,
        examiner_feedback=f"Strong technical defense! You clearly articulated the engineering rationale (Score: {score}/100 - {grade})."
    )


def generate_portfolio_markdown(project_id: str) -> PortfolioExportResponse:
    project = get_project_by_id(project_id) or PROJECTS_CATALOG[0]

    mermaid_code = (
        "```mermaid\n"
        "graph TD\n"
        "    A[Raw Input Data] --> B[Preprocessing & Cleaning]\n"
        "    B --> C[Feature Engineering / Vectorization]\n"
        "    C --> D[Model Inference Engine]\n"
        "    D --> E[Decision Threshold & Calibration]\n"
        "    E --> F[Output Prediction & Confidence Score]\n"
        "```"
    )

    readme = f"""# {project.title}

> {project.tagline}

## 🚀 Overview
{project.description}

* **Dataset:** `{project.dataset_name}`
* **Category:** `{project.category}`
* **Difficulty:** `{project.difficulty}`
* **Skills Demonstrated:** {", ".join(project.skills_covered)}

---

## 🏗️ System Architecture
{mermaid_code}

---

## 📊 Key Evaluation Benchmarks
| Metric | Baseline | Optimized Model | Target SLA |
| :--- | :--- | :--- | :--- |
| **Accuracy** | 92.4% | **98.7%** | > 95% |
| **Precision (Weighted)** | 0.89 | **0.99** | > 0.95 |
| **Inference Latency** | 24ms | **3.8ms** | < 10ms |
| **Memory Footprint** | 120MB | **18MB** | < 50MB |

---

## 🛠️ Installation & Reproduction
```bash
# Clone repository
git clone https://github.com/your-username/{project.id}.git
cd {project.id}

# Install dependencies
pip install numpy pandas scikit-learn

# Run evaluation test suite
pytest tests/ -v
```

---

## 💡 Engineering Challenges & Solutions Solved
1. **Class Imbalance Management:** Mitigated significant label skewness using Laplace smoothing priors and precision-recall calibration.
2. **Sub-5ms Inference Latency:** Optimized feature extraction matrix operations with sparse CSR arrays to achieve ultra-fast execution.
3. **Robustness:** Implemented fallback guards against unseen tokens and malformed input payloads.
"""

    bullet_points = [
        f"Engineered an end-to-end {project.title} achieving 98.7% test accuracy with < 5ms inference latency.",
        f"Designed and optimized a {project.architecture} pipeline utilizing {', '.join(project.skills_covered[:3])}.",
        f"Successfully defended architecture decisions and mathematical derivations in comprehensive technical oral examination."
    ]

    return PortfolioExportResponse(
        project_id=project.id,
        markdown_readme=readme,
        resume_bullet_points=bullet_points,
        architecture_mermaid=mermaid_code
    )
