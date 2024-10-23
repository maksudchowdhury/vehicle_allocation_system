# routes/allocation.py
from fastapi import APIRouter, HTTPException
from models.allocation import Allocation
from utils.db import allocation_collection
from datetime import date

router = APIRouter()

@router.post("/allocate", response_model=Allocation)
async def allocate_vehicle(allocation: Allocation):
    if allocation.date < date.today():
        raise HTTPException(status_code=400, detail="Cannot allocate for past dates")
    
    # Ensure vehicle is free on that day
    existing = await allocation_collection.find_one({"vehicle_id": allocation.vehicle_id, "date": allocation.date})
    if existing:
        raise HTTPException(status_code=400, detail="Vehicle already allocated for this date")

    await allocation_collection.insert_one(allocation.model_dump())
    return allocation.model_dump()

@router.put("/allocate/{allocation_id}", response_model=Allocation)
async def update_allocation(allocation_id: str, allocation: Allocation):
    # Update only before the allocation date
    existing = await allocation_collection.find_one({"_id": allocation_id})
    if not existing or existing["date"] < date.today():
        raise HTTPException(status_code=400, detail="Cannot update past or non-existing allocations")
    
    await allocation_collection.update_one({"_id": allocation_id}, {"$set": allocation.model_dump()})
    return allocation.model_dump()

@router.delete("/allocate/{allocation_id}")
async def delete_allocation(allocation_id: str):
    # Deletion only before the allocation date
    existing = await allocation_collection.find_one({"_id": allocation_id})
    if not existing or existing["date"] < date.today():
        raise HTTPException(status_code=400, detail="Cannot delete past or non-existing allocations")
    
    await allocation_collection.delete_one({"_id": allocation_id})
    return {"message": "Allocation deleted"}

@router.get("/allocate/getAll")
async def allocation_getAll():
    return await allocation_collection.find().to_list()