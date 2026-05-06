# Home Mortgage Review API

A lightweight backend API for mortgage application review, built with **FastAPI** and **SQLite**.

The system allows users to submit a loan application, calculate the Loan-to-Value ratio, store application records in a database, retrieve existing applications, update review decisions, and delete applications.

---

## Project Overview

This project is a small backend service designed to simulate a mortgage review workflow.

The API supports:

- Health check endpoint
- Loan-to-Value calculation
- Application creation
- SQLite database persistence
- Application listing
- Single application lookup
- Application status update
- Application deletion
- Automated testing with pytest

---

## Tech Stack

- Python
- FastAPI
- SQLite
- Pydantic
- pytest
- Uvicorn

---

## Project Structure

```text
HM_backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI routes and application entry point
│   ├── schemas.py       # Pydantic request and response models
│   ├── service.py       # Business logic for LTV calculation
│   └── database.py      # SQLite database connection and CRUD functions
│
├── test_main/
│   └── test_main.py     # API tests
│
├── pytest.ini           # pytest configuration
├── requirements.txt     # Python dependencies
└── README.md