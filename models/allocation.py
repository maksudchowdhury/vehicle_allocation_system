# models/allocation.py
from pydantic import BaseModel
from datetime import datetime

class Allocation(BaseModel):
    employee_id: str
    vehicle_id: str
    date: datetime