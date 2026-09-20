import asyncio
import logging
from app.core.database import connect_to_mongo, close_mongo_connection, get_database
from app.seed.seed_data import COURSES_DATA, LESSONS_DATA, QUIZZES_DATA, SKILLS_DATA

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("seed_runner")

async def seed_database():
    await connect_to_mongo()
    db = get_database()
    
    logger.info("Seeding courses...")
    for course in COURSES_DATA:
        await db.courses.update_one({"slug": course["slug"]}, {"$set": course}, upsert=True)
        
    logger.info("Seeding lessons...")
    for lesson in LESSONS_DATA:
        await db.lessons.update_one({"slug": lesson["slug"]}, {"$set": lesson}, upsert=True)
        
    logger.info("Seeding quizzes...")
    for quiz in QUIZZES_DATA:
        await db.quizzes.update_one({"id": quiz["id"]}, {"$set": quiz}, upsert=True)
        
    logger.info("Seeding skills...")
    for skill in SKILLS_DATA:
        await db.skills.update_one({"id": skill["id"]}, {"$set": skill}, upsert=True)
        
    logger.info("Seed process completed successfully!")
    await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(seed_database())
