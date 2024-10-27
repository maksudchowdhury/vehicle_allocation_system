# routes/vehicle.py
from fastapi import APIRouter, HTTPException
from models.vehicle import Vehicle
from utils.db import vehicle_collection
from bson import ObjectId
from utils.objid_str import objid_str

router = APIRouter()

@router.post("/vehicle", response_model=Vehicle)
async def create_vehicle(vehicle: Vehicle):
    await vehicle_collection.insert_one(vehicle.model_dump())
    return vehicle

@router.get("/vehicle/{vehicle_id}", response_model=Vehicle)
async def get_vehicle(vehicle_id: str):
    vehicle = await vehicle_collection.find_one({"_id": ObjectId(vehicle_id)})
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.get("/vehicle/")
async def get_all_vehicles():
    all_vehicles = await vehicle_collection.find().to_list()
    all_vehicles =[objid_str(each_vehicle) for each_vehicle in all_vehicles]
    return all_vehicles