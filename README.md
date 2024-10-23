# Vehicle Allocation System

## Description

The Vehicle Allocation System allows employees of a company to allocate vehicles for personal or official use on specific dates. The system ensures that a vehicle is not double-booked for the same date and that all vehicle bookings are properly managed. Each vehicle has a pre-assigned driver, and employees can only book vehicles that are free on the desired date. The system supports creating, updating, viewing, and deleting vehicle allocations, with appropriate constraints based on the allocation date.

The goal is to ensure smooth, efficient management of vehicle bookings and provide useful reports on allocation history. The system is optimized for performance under load and comes with proper documentation and testing.

---

## Features

- **Vehicle Allocation**: Allocate vehicles to employees for specific dates, ensuring no double bookings.
- **Allocation Modifications**: Update or delete allocations, but only before the allocation date.
- **History Reports**: View allocation history with filters like employee, vehicle, or date range.
- **Scalability**: Optimized for handling high load, ensuring smooth performance with 1,000 employees and vehicles.
- **Unrestricted API**: No authentication is required, making it open for all users.
- **Swagger Documentation**: Proper API documentation available through Swagger.

---

## CRUD Operations

### 1. **Create (C): Allocating a Vehicle**

- **Operation**: An employee allocates a vehicle for themselves on a specific day.
- **Conditions**:
  - The vehicle must not be allocated to anyone else on that same date.
- **Example**:
  Employee A wants to allocate **Vehicle 101** for **October 22, 2024**.
  The system checks if Vehicle 101 is already booked for that date.
  If it's free, the system creates the allocation with details like employee ID, vehicle ID, driver ID, and the date of allocation.

---

### 2. **Read (R): Checking Allocations and History**

- **Operation**: Employees or system admins can check:
  - Whether a vehicle is already allocated on a particular date.
  - The history of allocations for a particular employee, vehicle, or date range.
- **Example**:
  Employee A can query the system to check if **Vehicle 101** is free for **October 22, 2024** or view their own past allocations.
  An admin might want to filter and see how many allocations were made in the last month, or how often Vehicle 101 was used.

---

### 3. **Update (U): Modifying an Allocation**

- **Operation**: An employee can update their existing vehicle allocation.
- **Conditions**:
  - The modification (e.g., changing the date or vehicle) can only be done **before the allocation date**.
  - Once the allocation date has passed, no further changes are allowed.
- **Example**:
  Employee A initially allocated **Vehicle 101** for **October 22, 2024**.
  They want to switch to **Vehicle 102** or change the date to **October 23, 2024**.
  As long as they make this change **before October 22**, and Vehicle 102 is available, the system updates the allocation.

---

### 4. **Delete (D): Cancelling an Allocation**

- **Operation**: An employee can delete (cancel) an existing allocation.
- **Conditions**:
  - Deletion (cancellation) can only happen **before the allocation date**.
  - Once the date has passed, the record can't be deleted.
- **Example**:
  Employee A allocated **Vehicle 101** for **October 22, 2024**, but decides to cancel the reservation.
  They can cancel it as long as it's before October 22.
  The system removes the allocation record.

---

## Setup

1. **MongoDB Setup**:

   - Ensure MongoDB is running on your machine or use a cloud provider like MongoDB Atlas.
   - Update the connection details in the FastAPI application to connect to your MongoDB instance.

2. **Environment Variables**:

   - Set the MongoDB URI as follows:
     ```
     MONGODB_URI=mongodb://localhost:27017
     ```

3. **Project Dependencies**:

   - Install required Python packages using the `requirements.txt` file.

4. **Database Collections**:
   - The MongoDB database will need collections for **employees**, **vehicles**, **drivers**, and **allocations**.

---

## Running the Project

To run the project, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd vehicle-allocation-system
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI Application**:

   ```bash
   uvicorn main:app --reload
   ```

4. **Access the API Documentation**:
   Open your browser and go to `http://127.0.0.1:8000/docs` to view the Swagger API documentation.

---

## Project Structure

```bash
.
├── main.py                   # Entry point for the FastAPI app
├── models/
│   ├── employee.py            # Employee model and schema
│   ├── vehicle.py             # Vehicle model and schema
│   ├── driver.py              # Driver model and schema
│   ├── allocation.py          # Allocation model and schema
├── routes/
│   ├── employee.py            # Employee CRUD routes
│   ├── vehicle.py             # Vehicle CRUD routes
│   ├── driver.py              # Driver CRUD routes
│   ├── allocation.py          # Allocation CRUD routes
├── utils/
│   ├── db.py                  # MongoDB connection setup
│   ├── objid_str.py          # Custom validation logic
├── README.md                  # Project description and setup instructions
└── requirements.txt           # Project dependencies
```

---

## Deployment

### **Docker Deployment**:

- **Dockerfile**: Create a `Dockerfile` to package the FastAPI app.
  ```Dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY . .
  RUN pip install -r requirements.txt
  CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- **Build the Docker Image**:
  ```bash
  docker build -t vehicle-allocation-app .
  ```
- **Run the Docker Container**:

  ```bash
  docker run -d -p 8000:8000 vehicle-allocation-app
  ```

- **MongoDB**: Use MongoDB Atlas for cloud-based MongoDB services.

---

## Maintenance

- **Database Backups**: Regularly backup the MongoDB database using automated scripts or third-party services like **MongoDB Atlas**.

---

<br>

# **API Endpoints**

This document provides a detailed description of the API endpoints available in the Vehicle Allocation System.

## Base URL

All API routes are prefixed with `/api`.

## Endpoints

### 1. Employee Endpoints

#### Create an Employee

- **Endpoint:** `/api/employee`
- **Method:** `POST`
- **Description:** Adds a new employee to the system.
- **Request Body:**
  ```json
  {
    "name": "string",
    "department": "string",
    "contact": "string"
  }
  ```
- **Response:**
  ```json
  {
    "name": "string",
    "department": "string",
    "contact": "string"
  }
  ```

#### Get Employee Information

- **Endpoint:** `/api/employee/{employee_id}`
- **Method:** `GET`
- **Description:** Retrieves details of an employee by their ID.
- **Response:**
  ```json
  {
    "id": "string",
    "name": "string",
    "department": "string",
    "contact": "string"
  }
  ```

---

### 2. Vehicle Endpoints

#### Create a Vehicle

- **Endpoint:** `/api/vehicle`
- **Method:** `POST`
- **Description:** Adds a new vehicle to the system.
- **Request Body:**
  ```json
  {
    "license_plate": "string",
    "model": "string",
    "driver_name": "string",
    "driver_contact": "string"
  }
  ```
- **Response:**
  ```json
  {
    "license_plate": "string",
    "model": "string",
    "driver_name": "string",
    "driver_contact": "string"
  }
  ```

#### Get Vehicle Information

- **Endpoint:** `/api/vehicle/{vehicle_id}`
- **Method:** `GET`
- **Description:** Retrieves details of a vehicle by its ID.
- **Response:**
  ```json
  {
    "_id": "string",
    "license_plate": "string",
    "model": "string",
    "driver_name": "string",
    "driver_contact": "string"
  }
  ```

---

### 3. Allocation Endpoints

#### Allocate a Vehicle to an Employee

- **Endpoint:** `/api/allocate`
- **Method:** `POST`
- **Description:** Allocates a vehicle to an employee for a specific date, given that the vehicle is not already allocated for that date.
- **Request Body:**

  ```json
  {
    "employee_id": "string",
    "vehicle_id": "string",
    "date": "YYYY-MM-DD"
  }
  ```

- **Response:**
  ```json
  {
    "_id": "string",
    "employee_id": "string",
    "vehicle_id": "string",
    "date": "YYYY-MM-DD"
  }
  ```

#### Update an Allocation

- **Endpoint:** `/api/allocate/{allocation_id}`
- **Method:** `PUT`
- **Description:** Updates an existing allocation before the allocation date.
- **Request Body:**
  ```json
  {
    "employee_id": "string",
    "vehicle_id": "string",
    "date": "YYYY-MM-DD"
  }
  ```
- **Response:**
  ```json
  {
    "_id": "string",
    "employee_id": "string",
    "vehicle_id": "string",
    "date": "YYYY-MM-DD"
  }
  ```

#### Delete an Allocation

- **Endpoint:** `/api/allocate/{allocation_id}`
- **Method:** `DELETE`
- **Description:** Deletes an allocation, provided the date has not passed.

#### Get Allocation History

- **Endpoint:** `/api/allocations`
- **Method:** `GET`
- **Description:** Retrieves all allocation records with filters for employee, vehicle, and date range.
- **Filters:** `employee_id`, `vehicle_id`, `start_date`, `end_date`.
- **Response:**
  ```json
  [
    {
      "employee_id": "string",
      "vehicle_id": "string",
      "date": "YYYY-MM-DD"
    }
  ]
  ```

---

## Notes

- All endpoints are unrestricted and do not require authentication.
- The system prevents vehicles from being allocated to more than one employee on the same date.
