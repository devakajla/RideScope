import pandas as pd
from functools import lru_cache

@lru_cache()
def get_dataframe():
    df = pd.read_csv("../data/cleaned_bike_data.csv")
    df = df[df['trip_duration'] <= 60].copy()
    return df
