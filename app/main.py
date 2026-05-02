from fastapi import FastAPI
from app.schemas import LTVrequest,LTVresponse
from app.service import calculate_ltv

app = FastAPI(
    title="Home mortgage Review",
    description='',
    version='0.1.0'
)

@app.get('/health')
def health_check()->dict:
    return {"status": "OK",
            'service':'loan-backend-api',
            'version':'0.1.0'
    }

@app.post('/calculate-ltv',response_model=LTVresponse)
def calculate_ltv(request: LTVrequest)->LTVresponse:
    return calculate_ltv(request)

