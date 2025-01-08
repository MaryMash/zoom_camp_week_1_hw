# zoom_camp_week_1_hw

#### Question 1. Knowing docker tags
Question: Which tag has the following text? - Automatically remove the container when it exits

Answer: `--rm`

#### Question 2. Understanding docker first run
Question: What is version of the package wheel ?

Answer: 0.45.1

#### Question 3. Count records
Question: How many taxi trips were totally made on September 18th 2019?

Answer: 15612

Code: 
```
SELECT count(1)
FROM green_taxi_data
WHERE date_trunc('day', lpep_pickup_datetime) = '2019-09-18'
  AND date_trunc('day', lpep_dropoff_datetime) = '2019-09-18'
```
#### Question 4. Longest trip for each day
Question: Which was the pick up day with the longest trip distance?

Answer: 2019-09-26

Code: 
```
SELECT count(1)
FROM green_taxi_data
WHERE date_trunc('day', lpep_pickup_datetime) = '2019-09-18'
  AND date_trunc('day', lpep_dropoff_datetime) = '2019-09-18'
```

#### Question 5. Three biggest pick up Boroughs
Question: Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?

Answer: "Brooklyn" "Manhattan" "Queens"

Code: 
```
SELECT DISTINCT z."Borough"
FROM green_taxi_data d
JOIN taxi_zones z ON d."PULocationID" = z."LocationID"
WHERE date_trunc('day', d.lpep_pickup_datetime) = '2019-09-18'
GROUP BY 1
HAVING sum(total_amount) > 50000
```

#### Question 6. Largest tip
Question: For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?

Answer: JFK Airport

Code: 
```
SELECT "Zone"
FROM taxi_zones
WHERE "LocationID" =
    (SELECT d."DOLocationID"
     FROM green_taxi_data d
     JOIN taxi_zones z ON d."PULocationID" = z."LocationID"
     WHERE date_trunc('month', d.lpep_pickup_datetime) = '2019-09-01'
       AND z."Zone" = 'Astoria'
     ORDER BY tip_amount DESC
     LIMIT 1)
```

#### Question 7. Creating Resources
Answer: [command output](terraform_output.txt)