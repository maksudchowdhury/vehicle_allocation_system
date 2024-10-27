# models/employee.py
from pydantic import BaseModel
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    department: str
    contact: str
