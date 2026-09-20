import httpx
from typing import Dict, Any
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.config import settings
from app.core.database import get_database

router = APIRouter(prefix="/settings", tags=["Settings"])

@router.get("/system-status")
async def get_system_status(db: AsyncIOMotorDatabase = Depends(get_database)) -> Dict[str, Any]:
    # Check MongoDB
    mongo_ok = False
    try:
        await db.client.admin.command('ping')
        mongo_ok = True
    except Exception:
        pass
        
    # Check Ollama
    ollama_ok = False
    ollama_models = []
    try:
        async with httpx.AsyncClient(timeout=1.5) as client:
            resp = await client.get(f"{settings.OLLAMA_URL}/api/tags")
            if resp.status_code == 200:
                ollama_ok = True
                data = resp.json()
                ollama_models = [m.get("name") for m in data.get("models", [])]
    except Exception:
        pass
        
    return {
        "status": "healthy",
        "api_version": settings.VERSION,
        "database": {
            "connected": mongo_ok,
            "database_name": settings.DATABASE_NAME
        },
        "local_ai": {
            "ollama_connected": ollama_ok,
            "ollama_url": settings.OLLAMA_URL,
            "available_models": ollama_models,
            "note": "Install Ollama locally and run 'ollama serve' for Phase 6 local AI tutor features." if not ollama_ok else "Ollama detected and ready."
        }
    }
