from fastapi import FastAPI, HTTPException

from app.schemas import LTVrequest, LTVresponse, updateLTV
from app.service import calculate_ltv
from app.database import init_db, get_application, list_application, update_application,delete_application

app = FastAPI(
    title="Home Mortgage Review API",
    description="A backend API for loan application LTV calculation and risk review.",
    version="0.1.0"
)


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/health")
def health_check() -> dict:
    return {
        "status": "OK",
        "service": "loan-backend-api",
        "version": "0.1.0"
    }


@app.post("/calculate-ltv", response_model=LTVresponse)
def calculate_ltv_endpoint(request: LTVrequest) -> LTVresponse:
    return calculate_ltv(request)


@app.get("/applications")
def get_applications(limit: int = 50):
    return list_application(limit=limit)


@app.get("/applications/{application_id}", response_model=LTVresponse)
def get_application_id(application_id: str):
    application = get_application(application_id)

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )
    return application

@app.patch('/applications/{application_id}',response_model=LTVresponse)
def patch_application(
        application_id:str,
        request:updateLTV,
):
    updated_application_status=update_application(
        application_id=application_id,
        status=request.status,
        decision=request.decision
    )

    if updated_application_status is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return updated_application_status

@app.delete("/applications/{application_id}")
def delete_application_endpoint(application_id: str):
    deleted = delete_application(application_id)

    if deleted is False:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return {
        "message": "Application deleted successfully",
        "application_id": application_id
    }

