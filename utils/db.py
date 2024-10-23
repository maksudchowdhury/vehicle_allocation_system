from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from motor.motor_asyncio import AsyncIOMotorClient
# uri = "mongodb+srv://chowdhurycodes:wNbVymGHsnrfwaUG@vas.nrn80.mongodb.net/?retryWrites=true&w=majority"
uri = "mongodb+srv://maksudchowdhury:mongo2024@fastapi-mongo.ucwg0.mongodb.net/?retryWrites=true&w=majority&appName=fastapi-mongo"
# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
client = AsyncIOMotorClient(uri)
db=client["vas_db"]
employee_collection = db["employees_data"]
vehicle_collection = db["vehicles_data"]
allocation_collection = db["allocations_data"]