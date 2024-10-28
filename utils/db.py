from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from motor.motor_asyncio import AsyncIOMotorClient

uri = "mongodb+srv://maksudchowdhury:mongo2024@fastapi-mongo.ucwg0.mongodb.net/?retryWrites=true&w=majority&appName=fastapi-mongo"

client = AsyncIOMotorClient(uri)
db=client["vas_db"]
employee_collection = db["employees_data"]
vehicle_collection = db["vehicles_data"]
allocation_collection = db["allocations_data"]