# -------------stop cache generation-----------
import sys; sys.dont_write_bytecode = True
# ---------------------------------------------
from fastapi import FastAPI
from routes import employee, vehicle, allocation
from utils.db import client
from utils.db import employee_collection, vehicle_collection, allocation_collection

app=FastAPI()


app.include_router(employee.router, prefix="/api")
app.include_router(vehicle.router, prefix="/api")
app.include_router(allocation.router, prefix="/api")


# # POST endpoint to create an entry without a model
# @app.post("/create")
# async def create_entry(data: dict):
#     # Insert the data directly into MongoDB
#     result = await employee_collection.insert_one(data)
    
#     return {"inserted_id": str(result.inserted_id)}