from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from app.schemas.tutor import (
    TutorChatRequest,
    TutorChatResponse,
    TutorModelsResponse
)
from app.services.tutor_service import (
    generate_tutor_response,
    fetch_available_models
)

router = APIRouter(prefix="/tutor", tags=["AI Tutor"])

@router.post("/chat", response_model=TutorChatResponse)
async def chat_with_tutor(req: TutorChatRequest):
    """Interact with the Context-Aware AI Tutor across Socratic, Math Derivation, or Debugging modes."""
    try:
        return await generate_tutor_response(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Tutor interaction failed: {str(e)}")

@router.get("/models", response_model=TutorModelsResponse)
async def get_tutor_models(base_url: str = "http://localhost:11434"):
    """Query local Ollama instance for available LLM models and health status."""
    return await fetch_available_models(base_url)

@router.get("/presets")
async def get_context_presets():
    """Retrieve pre-built learning contexts and sample questions."""
    return {
        "modes": [
            {
                "id": "socratic",
                "name": "Socratic Guide",
                "icon": "🦉",
                "description": "Guides you through conceptual questions without spoiling full answers."
            },
            {
                "id": "explain_mistake",
                "name": "Explain My Mistake",
                "icon": "🔍",
                "description": "Analyzes why your code or math failed and teaches the fix."
            },
            {
                "id": "math_derivation",
                "name": "Math & Derivations",
                "icon": "📐",
                "description": "Step-by-step mathematical proofs, loss equations, and matrix calculus."
            },
            {
                "id": "code_review",
                "name": "Code Review & Performance",
                "icon": "⚡",
                "description": "Evaluates NumPy/PyTorch vectorization, broadcasting, and numerical stability."
            }
        ],
        "quick_questions": [
            "Why does Scaled Dot-Product Attention divide by √d_k?",
            "Derive the Ordinary Least Squares (OLS) Normal Equation step-by-step",
            "Why did my gradient explode to NaN during training?",
            "What is the mathematical difference between Gini Impurity and Entropy?",
            "How does L2 Ridge Regularization prevent multicollinearity singularities?",
            "Explain the geometric intuition of PCA eigenvectors"
        ]
    }
