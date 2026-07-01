from fastapi import APIRouter
from pydantic import BaseModel
from services.ml_service import predict_rider_type

router = APIRouter()

class RiderRequest(BaseModel):
    ride_type: str
    trip_duration: float
    hour: int
    day_of_week: str
    month: int
    distance_km: float

@router.post("/rider-type")
async def get_rider_prediction(req: RiderRequest):
    result = predict_rider_type(req.ride_type, req.trip_duration, req.hour, req.day_of_week, req.month, req.distance_km)
    return result
