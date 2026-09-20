import logging
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.config import settings

logger = logging.getLogger(__name__)

class DatabaseManager:
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

db_manager = DatabaseManager()

async def connect_to_mongo():
    logger.info("Connecting to MongoDB at %s...", settings.MONGODB_URL)
    try:
        db_manager.client = AsyncIOMotorClient(settings.MONGODB_URL)
        db_manager.db = db_manager.client[settings.DATABASE_NAME]
        # Ping the server
        await db_manager.client.admin.command('ping')
        logger.info("Successfully connected to MongoDB database '%s'", settings.DATABASE_NAME)
        
        # Ensure indexes
        await init_db_indexes(db_manager.db)
    except Exception as e:
        logger.error("Failed to connect to MongoDB: %s", str(e))
        raise e

async def close_mongo_connection():
    if db_manager.client:
        db_manager.client.close()
        db_manager.client = None
        db_manager.db = None

def get_database() -> AsyncIOMotorDatabase:
    if db_manager.db is None:
        db_manager.client = AsyncIOMotorClient(settings.MONGODB_URL)
        db_manager.db = db_manager.client[settings.DATABASE_NAME]
    return db_manager.db

async def init_db_indexes(db: AsyncIOMotorDatabase):
    """Ensure all required indexes exist for optimal query performance."""
    try:
        await db.users.create_index("email", unique=True)
        await db.courses.create_index("slug", unique=True)
        await db.courses.create_index("order")
        await db.lessons.create_index("slug", unique=True)
        await db.lessons.create_index([("course_slug", 1), ("order", 1)])
        await db.quizzes.create_index("lesson_slug")
        await db.progress.create_index([("user_id", 1), ("course_slug", 1)], unique=True)
        await db.daily_challenges.create_index("date", unique=True)
    except Exception as e:
        logger.warning("Error initializing indexes: %s", str(e))
