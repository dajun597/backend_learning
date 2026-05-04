from app.schemas import LTVresponse,LTVrequest
from uuid import uuid4
from datetime import datetime,timezone
from app.database import save_application

def calculate_ltv(request: LTVrequest)->LTVresponse:
    total_debt_after_loan=request.existing_mortgage+request.loan_amount
    available_equity=request.property_value-request.existing_mortgage
    ltv=total_debt_after_loan/request.property_value


    if ltv<0.15:
        risk_level = "LOW"
        decision = "Eligible for review"
        status = "PENDING_REVIEW"
    elif 0.15<ltv<0.30:
        risk_level = "MEDIUM"
        decision = "Eligible with standard review"
        status = "PENDING_REVIEW"
    elif 0.30<ltv<0.50:
        risk_level = "High"
        decision = "Requires careful underwriting review"
        status = "MANUAL_REVIEW_REQUIRED"
    else:
        risk_level = "DECLINE"
        decision = "LTV is too high"
        status = "DECLINED"

    application = {
        "application_id": str(uuid4()),
        "customer_id": request.customer_id,
        "property_value": request.property_value,
        "existing_mortgage": request.existing_mortgage,
        "loan_amount": request.loan_amount,
        "total_debt_after_loan": total_debt_after_loan,
        "available_equity": available_equity,
        "ltv": round(ltv, 4),
        "risk_level": risk_level,
        "decision": decision,
        "status": status,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    save_application(application)
    return LTVresponse(**application)


