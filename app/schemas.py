from pydantic import BaseModel, Field


class LTVrequest(BaseModel):
    property_value: float = Field(..., gt=0, description='mortgage property value')
    existing_mortgage: float = Field(..., gt=0, description='existing morgage amount')
    loan_amount: float = Field(..., gt=0, description='loan amount')


class LTVresponse(BaseModel):
    property_value: float
    existing_mortgage: float
    loan_amount: float
    total_debt_after_loan: float
    available_equity: float
    ltv: float
    risk_level: str
    descision: float