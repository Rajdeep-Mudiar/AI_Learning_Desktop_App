from typing import List, Dict, Any, Optional
from datetime import datetime, timezone
import uuid
from app.schemas.community import (
    CommunityPost,
    PostComment,
    CreatePostRequest,
    CareerPath,
    RoleSkillRequirement,
    CareerOverviewResponse
)

# In-memory community posts store
POSTS_STORE: List[CommunityPost] = [
    CommunityPost(
        id="post-1",
        title="Visualizing Attention Weights for Long Context Documents (Code + Diagram)",
        author_name="Sarah Chen",
        author_title="AI Research Fellow",
        author_avatar="👩‍🔬",
        category="Show & Tell",
        content="I built a custom visualizer for Scaled Dot-Product attention showing how query vectors attend to distant context tokens in 10k token windows. The sqrt(d_k) normalization really keeps the gradient signals stable!",
        code_snippet="scores = (Q @ K.T) / np.sqrt(d_k)\nattention = softmax(scores, axis=-1)\noutput = attention @ V",
        tags=["Transformers", "Attention", "Visualization"],
        upvotes=42,
        comments_count=2,
        created_at="2 hours ago",
        comments=[
            PostComment(
                id="c-1",
                author_name="Marcus Vance",
                author_avatar="👨‍💻",
                content="Awesome visualization! Did you try comparing this against FlashAttention kernel tiling?",
                created_at="1 hour ago",
                upvotes=5
            ),
            PostComment(
                id="c-2",
                author_name="Elena Rostova",
                author_avatar="👩‍🎓",
                content="The geometric intuition makes so much sense now. Thanks for sharing the code!",
                created_at="30 mins ago",
                upvotes=2
            )
        ]
    ),
    CommunityPost(
        id="post-2",
        title="Debugging Tip: Watch out for NaN Loss when training with standard MSE on unnormalized features",
        author_name="David K.",
        author_title="ML Engineer",
        author_avatar="👨‍🏫",
        category="Algorithm Debugging",
        content="Ran into a stubborn NaN gradient bug today during Ridge regression. Turns out one feature had variance 10,000x larger than others. Always run StandardScaler before fitting linear models!",
        tags=["Debugging", "StandardScaler", "Preprocessing"],
        upvotes=28,
        comments_count=1,
        created_at="4 hours ago",
        comments=[
            PostComment(
                id="c-3",
                author_name="Priya Patel",
                author_avatar="👩‍💻",
                content="Crucial reminder! Also make sure to fit the scaler ONLY on the training split to avoid data leakage.",
                created_at="2 hours ago",
                upvotes=9
            )
        ]
    )
]

CAREER_PATHS: List[CareerPath] = [
    CareerPath(
        id="applied-ml-engineer",
        role_title="Applied Machine Learning Engineer",
        average_salary="$165,000 / yr",
        market_demand="Very High",
        description="Designs, builds, and deploys predictive ML pipelines, feature stores, and real-time classification/regression microservices.",
        readiness_percentage=85,
        skills_required=[
            RoleSkillRequirement(skill_name="NumPy Matrix Operations & Vectorization", importance="Must Have", is_mastered=True, matching_course="Foundations of AI & Mathematics"),
            RoleSkillRequirement(skill_name="Supervised Learning & Hyperparameter Tuning", importance="Must Have", is_mastered=True, matching_course="Supervised Learning Mastery"),
            RoleSkillRequirement(skill_name="Model Evaluation & Diagnostic Curves (ROC, Confusion Matrix)", importance="Must Have", is_mastered=True, matching_course="Supervised Learning Mastery"),
            RoleSkillRequirement(skill_name="Subprocess & Safe Model Serving Pipelines", importance="Important", is_mastered=True, matching_course="AI Engineering Systems"),
            RoleSkillRequirement(skill_name="Real-Time Data Streaming & Feature Stores", importance="Good to Have", is_mastered=False, matching_course="MLOps & Scaled Systems")
        ]
    ),
    CareerPath(
        id="foundation-model-researcher",
        role_title="Foundation Model / LLM Researcher",
        average_salary="$210,000 / yr",
        market_demand="Very High",
        description="Develops novel Transformer architectures, attention optimizations, parameter-efficient fine-tuning (PEFT/LoRA), and pre-training scaling laws.",
        readiness_percentage=75,
        skills_required=[
            RoleSkillRequirement(skill_name="Scaled Dot-Product Attention Mechanics", importance="Must Have", is_mastered=True, matching_course="Deep Learning & Neural Architectures"),
            RoleSkillRequirement(skill_name="Backpropagation Calculus & Gradient Dynamics", importance="Must Have", is_mastered=True, matching_course="Deep Learning & Neural Architectures"),
            RoleSkillRequirement(skill_name="LoRA & Low-Rank Parameter Adaptation", importance="Must Have", is_mastered=True, matching_course="AI Research Mode"),
            RoleSkillRequirement(skill_name="Distributed GPU Training & FP8 Quantization", importance="Important", is_mastered=False, matching_course="Distributed AI Research")
        ]
    )
]

def list_posts() -> List[CommunityPost]:
    return POSTS_STORE

def create_community_post(req: CreatePostRequest) -> CommunityPost:
    new_post = CommunityPost(
        id=f"post-{uuid.uuid4().hex[:6]}",
        title=req.title,
        author_name="You (Student)",
        author_title="AI Learning Lab Member",
        author_avatar="🎓",
        category=req.category,
        content=req.content,
        code_snippet=req.code_snippet,
        tags=req.tags,
        upvotes=1,
        comments_count=0,
        created_at="Just now",
        comments=[]
    )
    POSTS_STORE.insert(0, new_post)
    return new_post

def upvote_post(post_id: str) -> Optional[CommunityPost]:
    for p in POSTS_STORE:
        if p.id == post_id:
            p.upvotes += 1
            return p
    return None

def get_career_overview() -> CareerOverviewResponse:
    return CareerOverviewResponse(
        career_paths=CAREER_PATHS,
        recommended_focus_areas=[
            "Complete Distributed GPU Training module to reach 100% Foundation Model Researcher readiness.",
            "Deploy your Spam Classifier as a Dockerized microservice for Applied ML portfolio strength."
        ]
    )
