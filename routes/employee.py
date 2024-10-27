# routes/employee.py
from fastapi import APIRouter, HTTPException
from models.employee import Employee
from utils.db import employee_collection
from bson.errors import InvalidId
from utils.objid_str import objid_str
from bson import ObjectId

router = APIRouter()

@router.post("/employee", response_model=Employee)
async def create_employee(employee: Employee):

    try:
        employee_collection.insert_one(employee.model_dump())
        return employee
    except Exception as error:
        return {"error": error}



@router.get("/employee/{employee_id}")
async def get_employee(employee_id: str):
    # Validate if employee_id is a valid ObjectId
    try:
        employee = await employee_collection.find_one({"_id": ObjectId(employee_id)})
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid employee ID format")

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return objid_str(employee)

# Similar update and delete routes


@router.get("/employee/")
async def get_all_employees():
    all_employees = await employee_collection.find().to_list()
    all_employees=[objid_str(each_employee) for each_employee in all_employees]
    return all_employees
