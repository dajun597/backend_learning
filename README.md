# Home Mortgage Review Backend API

A FastAPI backend project for processing home mortgage / loan applications.  
The API calculates Loan-to-Value (LTV), assigns a risk level, stores application records in a SQLite database, and supports basic CRUD operations.

---

## Project Overview

This project is a small backend service designed to demonstrate:

- FastAPI API development
- Pydantic request and response validation
- SQLite database integration
- CRUD operations
- Basic risk decision logic
- REST API design
- Swagger documentation for API testing

The backend allows users to create a loan application, calculate the LTV, save the result to a database, retrieve applications, update application status, and delete records.

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- SQLite
- Uvicorn
- Git / GitHub

---

## Project Structure

```text
app/
│
├── main.py          # FastAPI application and API endpoints
├── schemas.py       # Pydantic request and response models
├── service.py       # Business logic for LTV calculation and risk decision
├── database.py      # SQLite database connection and CRUD functions
└── loan_application.db   # Local SQLite database file, generated automatically