from fastapi import APIRouter
from services.data_service import get_dataframe

router = APIRouter()

@router.get("/top")
async def get_top_stations(limit: int = 10):
    df = get_dataframe()
    top = df.groupby('start_station_name').agg(
        trip_count=('ride_id', 'count'),
        lat=('start_lat', 'mean'),
        lng=('start_lng', 'mean')
    ).sort_values('trip_count', ascending=False).head(limit).reset_index()
    return {"stations": top.to_dict('records')}

@router.get("/map-data")
async def get_map_data():
    df = get_dataframe()
    stations = df.groupby('start_station_name').agg(
        lat=('start_lat', 'mean'),
        lng=('start_lng', 'mean'),
        member_trips=('user_type', lambda x: (x == 'member').sum()),
        casual_trips=('user_type', lambda x: (x == 'casual').sum())
    ).reset_index()
    return {"stations": stations.to_dict('records')}
