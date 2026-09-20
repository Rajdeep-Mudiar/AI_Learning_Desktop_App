from fastapi import APIRouter
from app.api.v1 import (
    auth, courses, lessons, quizzes, skills,
    dashboard, settings, simulations, diagnostics,
    sandbox, challenges, datasets, experiments,
    deep_learning, tutor, projects, achievements,
    research, interviews, hackathons, community, career
)
from app.core.database import get_database
from app.seed.seed_data import COURSES_DATA, LESSONS_DATA, QUIZZES_DATA, SKILLS_DATA

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(courses.router)
api_router.include_router(lessons.router)
api_router.include_router(quizzes.router)
api_router.include_router(skills.router)
api_router.include_router(dashboard.router)
api_router.include_router(settings.router)
api_router.include_router(simulations.router)
api_router.include_router(diagnostics.router)
api_router.include_router(sandbox.router)
api_router.include_router(challenges.router)
api_router.include_router(datasets.router)
api_router.include_router(experiments.router)
api_router.include_router(deep_learning.router)
api_router.include_router(tutor.router)
api_router.include_router(projects.router)
api_router.include_router(achievements.router)
api_router.include_router(research.router)
api_router.include_router(interviews.router)
api_router.include_router(hackathons.router)
api_router.include_router(community.router)
api_router.include_router(career.router)

@api_router.post("/seed/reset", tags=["Seed"])
async def reset_seed_data():
    db = get_database()
    for course in COURSES_DATA:
        await db.courses.update_one({"slug": course["slug"]}, {"$set": course}, upsert=True)
    for lesson in LESSONS_DATA:
        await db.lessons.update_one({"slug": lesson["slug"]}, {"$set": lesson}, upsert=True)
    for quiz in QUIZZES_DATA:
        await db.quizzes.update_one({"id": quiz["id"]}, {"$set": quiz}, upsert=True)
    for skill in SKILLS_DATA:
        await db.skills.update_one({"id": skill["id"]}, {"$set": skill}, upsert=True)
    return {"message": "Curriculum seed data successfully refreshed!"}
