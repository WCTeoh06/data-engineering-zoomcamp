import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://root:root@localhost:5433/ny_taxi")
df = pd.read_csv("taxi_zone_lookup.csv")
df.to_sql("zones", engine, if_exists="replace", index=False)
print("rows loaded:", len(df))
