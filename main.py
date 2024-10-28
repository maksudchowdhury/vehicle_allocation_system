# -------------stop cache generation-----------
import sys; sys.dont_write_bytecode = True
# ---------------------------------------------
from fastapi import FastAPI
from routes import employee, vehicle, allocation


app=FastAPI()


app.include_router(employee.router, prefix="/api")
app.include_router(vehicle.router, prefix="/api")
app.include_router(allocation.router, prefix="/api")
