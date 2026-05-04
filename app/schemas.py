from pydantic import BaseModel, Field


class LTVrequest(BaseModel):
    customer_id:str = Field(...,min_length=1,description='customer name')
    property_value: float = Field(..., gt=0, description='mortgage property value')
    existing_mortgage: float = Field(..., ge=0, description='existing morgage amount')
    loan_amount: float = Field(..., gt=0, description='loan amount')


class LTVresponse(BaseModel):
    application_id: str
    customer_id: str
    property_value: float
    existing_mortgage: float
    loan_amount: float
    total_debt_after_loan: float
    available_equity: float
    ltv: float
    risk_level: str
    decision: str
    status: str
    created_at: str