# routes/allocation.py
from fastapi import APIRouter, HTTPException
from models.allocation import Allocation
from utils.db import allocation_collection,employee_collection
from utils.objid_str import objid_str
from datetime import datetime,date
from bson import ObjectId

router = APIRouter()

@router.post("/allocate/vehicle/{employee_id}", response_model=Allocation)
async def allocate_vehicle(employee_id,allocation: Allocation):

    #ensure user is valid
    valid_uesr= await employee_collection.find_one({"_id": ObjectId(employee_id)})
    if not valid_uesr:
        raise HTTPException(status_code=400, detail="Id for employee is not valid")

    # allocation_date = datetime.combine(allocation.date, datetime.min.time())
    print(allocation.date, datetime.today())
    if allocation.date < datetime.today():
        raise HTTPException(status_code=400, detail="Cannot allocate for past dates")
    
    # Ensure vehicle is free on that day
    existing = await allocation_collection.find_one({"vehicle_id": allocation.vehicle_id, "date": allocation.date})
    if existing:
        raise HTTPException(status_code=400, detail="Vehicle already allocated for this date")
    
    allocation_data = allocation.model_dump()
    allocation_data['date'] = allocation.date

    await allocation_collection.insert_one(allocation_data)

    return allocation

@router.put("/allocate/{allocation_id}", response_model=Allocation)
async def update_allocation(allocation_id: str, allocation: Allocation):
    # Update only before the allocation date
    existing = await allocation_collection.find_one({"_id": ObjectId(allocation_id)})


    if not existing:
        raise HTTPException(status_code=400, detail="Cannot update non-existing allocations")
    
    if existing["date"]< datetime.today():
        raise HTTPException(status_code=400, detail="Cannot update past allocations")
    
    updated_data = allocation.model_dump()

    await allocation_collection.update_one({"_id": ObjectId(allocation_id)}, {"$set": updated_data})

    return allocation

@router.delete("/allocate/{allocation_id}")
async def delete_allocation(allocation_id: str):
    # Deletion only before the allocation date
    existing = await allocation_collection.find_one({"_id": ObjectId(allocation_id)})

    if not existing:
        raise HTTPException(status_code=400, detail="Cannot update non-existing allocations")
    
    if existing["date"]< datetime.today():
        raise HTTPException(status_code=400, detail="Cannot update past allocations")
    
    await allocation_collection.delete_one({"_id": ObjectId(allocation_id)})
    return {"message": "Allocation deleted"}

@router.get("/allocate/getAll")
async def get_all_allocations():
    all_allocations = await allocation_collection.find().to_list()
    all_allocations = [objid_str(single_allocation) for single_allocation in all_allocations]
    return all_allocations