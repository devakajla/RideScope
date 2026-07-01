from fastapi import APIRouter
from services.data_service import get_dataframe

router = APIRouter()

@router.get("/summary")
async def get_summary():
    df = get_dataframe()
    return {
        "total_rides": len(df),
        "avg_duration_min": round(df['trip_duration'].mean(), 2),
        "member_count": int((df['user_type'] == 'member').sum()),
        "casual_count": int((df['user_type'] == 'casual').sum()),
        "top_bike_type": df['ride_type'].value_counts().index[0]
    }

@router.get("/trends")
async def get_trends(group_by: str = "hour"):
    df = get_dataframe()
    grouped = df.groupby([group_by, 'user_type'])['ride_id'].count().unstack(fill_value=0)
    return {
        "labels": grouped.index.tolist(),
        "member": grouped.get('member', []).tolist(),
        "casual": grouped.get('casual', []).tolist()
    }
