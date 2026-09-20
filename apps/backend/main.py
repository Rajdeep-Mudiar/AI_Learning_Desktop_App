from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import connect_to_mongo, close_mongo_connection, get_database
from app.core.logging import setup_logging
from app.api.v1.router import api_router
from app.seed.seed_data import COURSES_DATA, LESSONS_DATA, QUIZZES_DATA, SKILLS_DATA

setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Connect to DB and auto-seed if empty
    await connect_to_mongo()
    db = get_database()
    
    # Check if courses exist, if not seed initial curriculum
    course_count = await db.courses.count_documents({})
    if course_count == 0:
        for course in COURSES_DATA:
            await db.courses.update_one({"slug": course["slug"]}, {"$set": course}, upsert=True)
        for lesson in LESSONS_DATA:
            await db.lessons.update_one({"slug": lesson["slug"]}, {"$set": lesson}, upsert=True)
        for quiz in QUIZZES_DATA:
            await db.quizzes.update_one({"id": quiz["id"]}, {"$set": quiz}, upsert=True)
        for skill in SKILLS_DATA:
            await db.skills.update_one({"id": skill["id"]}, {"$set": skill}, upsert=True)
            
    yield
    # Shutdown
    await close_mongo_connection()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for local Tauri desktop & Vite dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/health")
async def health_check():
    return {"status": "ok", "app": settings.PROJECT_NAME, "version": settings.VERSION}

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.getenv("PORT", 8001))
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)

