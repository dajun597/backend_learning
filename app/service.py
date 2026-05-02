from app.schemas import LTVresponse,LTVrequest

def calculate_ltv(request: LTVrequest)->LTVresponse:
    total_debt_after_loan=request.existing_mortgage+request.loan_amount
    available_equity=request.property_value-request.existing_mortgage
    ltv=total_debt_after_loan/request.property_value


    if ltv<0.15:
        risk_level = "LOW"
        decision = "Eligible for review"
    elif 0.15<ltv<0.30:
        risk_level = "MEDIUM"
        decision = "Eligible with standard review"
    elif 0.30<ltv<0.50:
        risk_level = "High"
        decision = "Requires careful underwriting review"
    else:
        risk_level = "DECLINE"
        decision = "LTV is too high"

    return LTVresponse(
        property_value=request.property_value,
        existing_mortgage=request.existing_mortgage,
        loan_amount=request.loan_amount,
        total_debt_after_loan=total_debt_after_loan,
        available_equity=available_equity,
        ltv=round(ltv, 4),
        risk_level=risk_level,
        decision=decision
    )


