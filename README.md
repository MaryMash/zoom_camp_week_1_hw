# zoom_camp_week_1_hw

#### Question 1. Understanding docker first run
Question: What's the version of pip in the image?

Answer: `24.3.1`

#### Question 2. Understanding Docker networking and docker-compose
Question: Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

Answer: `postgres:5432`

#### Question 3. Trip Segmentation Count
Answer: `104,802; 198,924; 109,603; 27,678; 35,189`

Code: 
```
SELECT CASE
           WHEN trip_distance <= 1 THEN 'up to 1'
           WHEN trip_distance > 1
                AND trip_distance <= 3 THEN 'up to 3'
           WHEN trip_distance > 3
                AND trip_distance <= 7 THEN 'up to 7'
           WHEN trip_distance > 7
                AND trip_distance <= 10 THEN 'up to 10'
           ELSE 'over 10'
       END AS SEGMENT,
       count(*)
FROM green_taxi_data gtd
WHERE date_trunc('month', lpep_pickup_datetime) = '2019-10-01'
  AND date_trunc('month', lpep_dropoff_datetime) = '2019-10-01'
GROUP BY 1;
```
#### Question 4. Longest trip for each day
Answer: `2019-10-31`

Code: 
```
SELECT date_trunc('day', lpep_pickup_datetime) AS lpep_pickup,
       max(trip_distance) AS max_distance
FROM green_taxi_data gtd 
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
```

#### Question 5. Three biggest pick up Boroughs

Answer: `East Harlem North, East Harlem South, Morningside Heights`

Code: 
```
SELECT taxi_zones."Zone",
       sum(total_amount) AS total
FROM green_taxi_data
JOIN taxi_zones ON green_taxi_data."PULocationID" = taxi_zones."LocationID"
WHERE date_trunc('day', lpep_pickup_datetime) = '2019-10-18'
GROUP BY 1
HAVING sum(total_amount) > 13000
```

#### Question 6. Largest tip

Answer: `JFK Airport`

Code: 
```
SELECT "Zone"
FROM taxi_zones
WHERE "LocationID" =
    (SELECT d."DOLocationID"
     FROM green_taxi_data d
     JOIN taxi_zones z ON d."PULocationID" = z."LocationID"
     WHERE date_trunc('month', d.lpep_pickup_datetime) = '2019-10-01'
       AND z."Zone" = 'East Harlem North'
     ORDER BY tip_amount DESC
     LIMIT 1)
```

#### Question 7. Creating Resources

Answer: `terraform init, terraform apply -auto-aprove, terraform destroy`