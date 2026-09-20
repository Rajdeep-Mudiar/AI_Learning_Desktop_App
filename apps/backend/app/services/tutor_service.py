import httpx
from typing import List, Dict, Any, Optional
from app.schemas.tutor import (
    TutorChatRequest,
    TutorChatResponse,
    TutorModelsResponse,
    OllamaModelItem
)

# Mode System Directives
MODE_PROMPTS = {
    "socratic": (
        "You are an inspiring, rigorous AI & Machine Learning Professor using the Socratic method.\n"
        "RULES:\n"
        "1. DO NOT immediately give the final solution or entire code blocks.\n"
        "2. Guide the student by asking 1-2 probing diagnostic questions that nudge them toward realizing the answer.\n"
        "3. Provide intuition and visual analogies before mathematical notation.\n"
        "4. Encourage the student to think through tensor shapes and computational graphs."
    ),
    "explain_mistake": (
        "You are an expert AI debugging mentor.\n"
        "RULES:\n"
        "1. Directly pinpoint the mathematical or logical flaw in the student's code or reasoning.\n"
        "2. Explain WHY it failed (e.g. broadcast shape mismatch, exploding gradient, lack of normalization, data leakage).\n"
        "3. Offer a corrected conceptual framework without making the student feel discouraged."
    ),
    "math_derivation": (
        "You are a mathematical machine learning researcher.\n"
        "RULES:\n"
        "1. Provide step-by-step mathematical proofs and derivations.\n"
        "2. Always verify and annotate tensor dimensions (e.g. X in R^(N x D)).\n"
        "3. Connect the algebraic equations to geometric intuition (e.g. hyperplane projections, gradient contours)."
    ),
    "code_review": (
        "You are a Senior MLOps and PyTorch/NumPy Systems Engineer.\n"
        "RULES:\n"
        "1. Review the provided code for vectorization (eliminating Python for-loops with NumPy/PyTorch).\n"
        "2. Check numerical stability (e.g., log-sum-exp, epsilon in denominators).\n"
        "3. Provide clean, idiomatic Python snippets with typing and docstrings."
    )
}

async def fetch_available_models(base_url: str = "http://localhost:11434") -> TutorModelsResponse:
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            resp = await client.get(f"{base_url}/api/tags")
            if resp.status_code == 200:
                data = resp.json()
                models = [
                    OllamaModelItem(
                        name=m.get("name", "unknown"),
                        size=str(round(m.get("size", 0) / (1024**3), 1)) + " GB" if m.get("size") else None,
                        family=m.get("details", {}).get("family", "LLM"),
                        is_available=True
                    )
                    for m in data.get("models", [])
                ]
                default_m = models[0].name if models else "llama3"
                return TutorModelsResponse(
                    available_models=models,
                    is_ollama_online=True,
                    default_model=default_m
                )
    except Exception:
        pass

    # Fallback offline preset models
    fallback_models = [
        OllamaModelItem(name="llama3:latest", size="4.7 GB", family="llama", is_available=False),
        OllamaModelItem(name="qwen2.5-coder:7b", size="4.4 GB", family="qwen2", is_available=False),
        OllamaModelItem(name="mistral:latest", size="4.1 GB", family="mistral", is_available=False),
        OllamaModelItem(name="gemma2:2b", size="1.6 GB", family="gemma2", is_available=False),
        OllamaModelItem(name="phi3:mini", size="2.2 GB", family="phi3", is_available=False),
    ]
    return TutorModelsResponse(
        available_models=fallback_models,
        is_ollama_online=False,
        default_model="llama3:latest"
    )


def generate_heuristic_tutor_response(req: TutorChatRequest) -> TutorChatResponse:
    """High-fidelity contextual fallback engine when local Ollama daemon is offline."""
    query = req.message.lower()
    mode = req.mode
    ctx = req.context

    # Socratic Knowledge Base
    if "attention" in query or "sqrt" in query or "scaled" in query:
        if mode == "socratic":
            ans = (
                "### 🔍 Let's examine the scaling factor in Attention:\n\n"
                "In Scaled Dot-Product Attention, we compute:\n"
                "$$\\mathbf{A} = \\text{Softmax}\\left(\\frac{Q K^T}{\\sqrt{d_k}}\\right) V$$\n\n"
                "**Consider this thought experiment:**\n"
                "1. If $Q$ and $K$ are vectors of dimension $d_k = 512$ with components having mean 0 and variance 1, what is the expected variance of their dot product $Q \\cdot K = \\sum_{i=1}^{d_k} q_i k_i$?\n"
                "2. When dot product values grow extremely large in magnitude (e.g. $+50$ or $-50$), what happens to the gradients of the $\\text{Softmax}$ function?\n\n"
                "👉 *Hint:* Recall where the derivative of $\\text{Softmax}$ vanishes in the saturation regions."
            )
        else:
            ans = (
                "### 📐 Why Attention divides by $\\sqrt{d_k}$:\n\n"
                "1. **Variance Growth**: If $q_i, k_i \\sim \\mathcal{N}(0, 1)$ are independent, the sum $z = \\sum_{i=1}^{d_k} q_i k_i$ has mean $0$ and **variance $d_k$**.\n"
                "2. **Softmax Saturation**: For large $d_k$ (e.g., $d_k=64$ or $512$), unscaled dot products yield large magnitudes. The $\\text{Softmax}$ function saturates to near 1 for the maximum and 0 elsewhere, resulting in **vanishing gradients** during backpropagation.\n"
                "3. **Stabilization**: Dividing by $\\sqrt{d_k}$ normalizes the variance back to $1.0$, keeping softmax in its active gradient region."
            )
        followups = [
            "What happens if we remove the softmax and use linear attention?",
            "How does Multi-Head Attention differ from Single-Head Attention?"
        ]
        concepts = ["Scaled Dot-Product Attention", "Softmax Saturation", "Variance Scaling", "Vanishing Gradients"]

    elif "gradient" in query and ("explod" in query or "vanish" in query or "zero" in query):
        ans = (
            "### ⚡ Gradient Dynamics & Stability:\n\n"
            "When training deep networks, backpropagation propagates gradients via the chain rule:\n"
            "$$\\frac{\\partial L}{\\partial W^{(1)}} = \\delta^{(L)} \\prod_{l=2}^{L} \\left( W^{(l)T} \\cdot \\sigma'(z^{(l)}) \\right) \\cdot x^T$$\n\n"
            "**Key Questions to Diagnose Your Model:**\n"
            "- Are you using **Sigmoid** in deep hidden layers where $\\max \\sigma'(z) = 0.25$ causes exponential shrinkage?\n"
            "- What is your weight initialization scheme (He vs Xavier)?\n"
            "- Are you using **Residual Connections (Skip Connections)** or **Layer Normalization**?"
        )
        followups = [
            "How does Gradient Clipping prevent numerical overflows?",
            "Why does ReLU solve the vanishing gradient problem for positive activations?"
        ]
        concepts = ["Backpropagation Chain Rule", "Gradient Clipping", "He Initialization", "Residual Connections"]

    elif "ols" in query or "normal equation" in query or "linear regression" in query:
        ans = (
            "### 📊 Ordinary Least Squares (OLS) Normal Equation:\n\n"
            "We wish to minimize the residual sum of squares:\n"
            "$$L(\\theta) = \\frac{1}{2} \\|X\\theta - y\\|^2 = \\frac{1}{2}(X\\theta - y)^T (X\\theta - y)$$\n\n"
            "Taking the gradient with respect to parameter vector $\\theta$:\n"
            "$$\\nabla_\\theta L(\\theta) = X^T(X\\theta - y) = X^T X\\theta - X^T y = 0$$\n\n"
            "Solving for $\\theta$ yields the closed-form solution:\n"
            "$$\\mathbf{\\theta = (X^T X)^{-1} X^T y}$$\n\n"
            "⚠️ **Gotcha:** If features are perfectly collinear (multicollinearity) or $N < D$, $X^T X$ is singular (non-invertible). That is why we use Ridge Regularization $(X^T X + \\lambda I)^{-1}$ or the Moore-Penrose pseudoinverse `np.linalg.pinv`."
        )
        followups = [
            "Why is gradient descent preferred over the Normal Equation for huge datasets (N > 100,000)?",
            "How does L2 Ridge regularization guarantee that the matrix is invertible?"
        ]
        concepts = ["Normal Equation", "Moore-Penrose Pseudoinverse", "Multicollinearity", "Singular Matrices"]

    else:
        # Context-aware general answer
        lesson_context_str = f" in relation to **{ctx.current_lesson_title}**" if ctx and ctx.current_lesson_title else ""
        ans = (
            f"### 🤖 AI Tutor Response{lesson_context_str}\n\n"
            f"You asked: *\"{req.message}\"*\n\n"
            "In machine learning systems, we structure problem-solving along four foundational pillars:\n"
            "1. **Mathematical Representation**: How the loss function and hypothesis class are formulated.\n"
            "2. **Optimization Dynamics**: How gradients travel through parameters (e.g. Adam, SGD, Backpropagation).\n"
            "3. **Generalization & Regularization**: Balancing bias vs variance ($L_1/L_2$, Dropout, Early Stopping).\n"
            "4. **Vectorized Computation**: Ensuring matrix shapes $(N \\times D)$ align without computational bottlenecks.\n\n"
            "How would you like to explore this concept further?"
        )
        followups = [
            "Walk me through the mathematical derivation step-by-step",
            "Show me a clean NumPy vectorized implementation",
            "Give me a challenge problem to test my understanding"
        ]
        concepts = ["Optimization", "Generalization", "Vectorization", "Loss Formulation"]

    return TutorChatResponse(
        response=ans,
        mode_used=mode,
        provider_used="heuristic_local (Offline Ready)",
        model_used="AI Lab Semantic Reasoning Engine",
        suggested_followups=followups,
        referenced_concepts=concepts
    )


async def generate_tutor_response(req: TutorChatRequest) -> TutorChatResponse:
    # 1. Try Ollama local inference if provider is "auto" or "ollama"
    if req.provider in ["auto", "ollama"]:
        try:
            system_prompt = MODE_PROMPTS.get(req.mode, MODE_PROMPTS["socratic"])
            
            # Ground with context if provided
            if req.context:
                if req.context.current_lesson_title:
                    system_prompt += f"\nActive Student Lesson: {req.context.current_lesson_title}"
                if req.context.active_code:
                    system_prompt += f"\nActive Student Code:\n```python\n{req.context.active_code}\n```"
                if req.context.active_error:
                    system_prompt += f"\nActive Error Traceback:\n{req.context.active_error}"
                if req.context.recent_quiz_mistake:
                    system_prompt += f"\nRecent Quiz Concept Mistake: {req.context.recent_quiz_mistake}"

            messages = [{"role": "system", "content": system_prompt}]
            for msg in req.history[-6:]:
                messages.append({"role": msg.role, "content": msg.content})
            messages.append({"role": "user", "content": req.message})

            ollama_url = req.ollama_base_url or "http://localhost:11434"
            model_name = req.model_name or "llama3"

            async with httpx.AsyncClient(timeout=15.0) as client:
                resp = await client.post(
                    f"{ollama_url}/api/chat",
                    json={
                        "model": model_name,
                        "messages": messages,
                        "stream": False,
                        "options": {
                            "temperature": 0.4 if req.mode == "math_derivation" else 0.7
                        }
                    }
                )
                if resp.status_code == 200:
                    data = resp.json()
                    ai_content = data.get("message", {}).get("content", "")
                    if ai_content:
                        return TutorChatResponse(
                            response=ai_content,
                            mode_used=req.mode,
                            provider_used="ollama",
                            model_used=model_name,
                            suggested_followups=[
                                "Can you explain this with a visual diagram?",
                                "What is the common failure mode for this?",
                                "Show me the mathematical proof"
                            ],
                            referenced_concepts=["Local Ollama Inference", req.mode.replace("_", " ").title()]
                        )
        except Exception:
            # Fall back to heuristic reasoning engine
            pass

    return generate_heuristic_tutor_response(req)
