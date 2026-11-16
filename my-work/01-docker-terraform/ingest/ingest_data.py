import pandas as pd
from sqlalchemy import create_engine

file = "yellow_tripdata_2021-01.csv.gz"
engine = create_engine("postgresql://root:root@localhost:5433/ny_taxi")

chunks = pd.read_csv(
    file,
    iterator=True,
    chunksize=100000,
    parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"],
)

first = True
total = 0
for chunk in chunks:
    if first:
        chunk.head(0).to_sql("yellow_taxi_data", engine, if_exists="replace", index=False)
        first = False
    chunk.to_sql("yellow_taxi_data", engine, if_exists="append", index=False)
    total += len(chunk)
    print("inserted so far:", total)
