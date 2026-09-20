from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class ChatMessage(BaseModel):
    role: str  # "user", "assistant", "system"
    content: str
    timestamp: Optional[str] = None

class TutorContext(BaseModel):
    current_lesson_title: Optional[str] = None
    current_lesson_slug: Optional[str] = None
    active_code: Optional[str] = None
    active_error: Optional[str] = None
    recent_quiz_mistake: Optional[str] = None
    student_level: Optional[str] = "intermediate"

class TutorChatRequest(BaseModel):
    message: str
    history: List[ChatMessage] = Field(default_factory=list)
    mode: str = "socratic"  # "socratic", "explain_mistake", "math_derivation", "code_review"
    provider: str = "auto"  # "auto", "ollama", "heuristic_local"
    model_name: Optional[str] = "llama3"
    ollama_base_url: Optional[str] = "http://localhost:11434"
    context: Optional[TutorContext] = None

class TutorChatResponse(BaseModel):
    response: str
    mode_used: str
    provider_used: str
    model_used: str
    suggested_followups: List[str] = Field(default_factory=list)
    referenced_concepts: List[str] = Field(default_factory=list)

class OllamaModelItem(BaseModel):
    name: str
    size: Optional[str] = None
    family: Optional[str] = None
    is_available: bool = True

class TutorModelsResponse(BaseModel):
    available_models: List[OllamaModelItem]
    is_ollama_online: bool
    default_model: str
