from fastapi import FastAPI
from services.ml_service import load_models
from fastapi.middleware.cors import CORSMiddleware
from routers import analytics, predict_duration, predict_rider, stations

app = FastAPI(title="RideScope API", version="1.0.0")
@app.on_event("startup")
async def startup():
    load_models()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])
app.include_router(predict_duration.router, prefix="/api/predict", tags=["Predictions"])
app.include_router(predict_rider.router, prefix="/api/predict", tags=["Predictions"])
app.include_router(stations.router, prefix="/api/stations", tags=["Stations"])

@app.get("/")
async def root():
    return {"message": "RideScope API is running"}
