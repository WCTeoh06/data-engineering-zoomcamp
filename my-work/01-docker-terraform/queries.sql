-- Clean view: keep only January 2021 pickups (24 rows excluded from raw data)
CREATE VIEW yellow_taxi_clean AS
SELECT *
FROM yellow_taxi_data
WHERE tpep_pickup_datetime >= '2021-01-01'
  AND tpep_pickup_datetime <  '2021-02-01';

-- Busiest pickup zones
SELECT z."Zone", count(*) AS trips
FROM yellow_taxi_clean t
JOIN zones z ON t."PULocationID" = z."LocationID"
GROUP BY 1
ORDER BY trips DESC
LIMIT 5;
