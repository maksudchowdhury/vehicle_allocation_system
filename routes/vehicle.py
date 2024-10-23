# routes/vehicle.py
from fastapi import APIRouter, HTTPException
from models.vehicle import Vehicle
from utils.db import db

router = APIRouter()

@router.post("/vehicle", response_model=Vehicle)
async def create_vehicle(vehicle: Vehicle):
    await db.vehicles.insert_one(vehicle.model_dump())
    return vehicle

@router.get("/vehicle/{vehicle_id}", response_model=Vehicle)
async def get_vehicle(vehicle_id: str):
    vehicle = await db.vehicles.find_one({"id": vehicle_id})
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle
