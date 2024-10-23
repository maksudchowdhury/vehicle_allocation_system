# models/allocation.py
from pydantic import BaseModel
from datetime import date

class Allocation(BaseModel):
    employee_id: str
    vehicle_id: str
    date: date
