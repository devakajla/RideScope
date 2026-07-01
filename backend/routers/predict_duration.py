from fastapi import APIRouter
from pydantic import BaseModel
from services.ml_service import predict_duration

router = APIRouter()

class DurationRequest(BaseModel):
    ride_type: str
    hour: int
    day_of_week: str
    month: int
    distance_km: float

@router.post("/duration")
async def get_duration_prediction(req: DurationRequest):
    result = predict_duration(req.ride_type, req.hour, req.day_of_week, req.month, req.distance_km)
    return {"predicted_duration_min": result}
