import pytest_asyncio
from app.core.database import connect_to_mongo, close_mongo_connection

@pytest_asyncio.fixture(scope="function", autouse=True)
async def setup_test_db():
    await connect_to_mongo()
    yield
    await close_mongo_connection()
