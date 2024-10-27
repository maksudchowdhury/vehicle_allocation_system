# models/vehicle.py
from pydantic import BaseModel
from pydantic import BaseModel

class Vehicle(BaseModel):
    license_plate: str
    model: str
    driver_name: str  # Pre-assigned driver
    driver_contact: str
