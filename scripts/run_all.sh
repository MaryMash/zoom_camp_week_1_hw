#!/bin/sh

python ./scripts/load_taxi_data.py\
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db=ny_taxi \
    --table_name=green_taxi_data \
    --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz" \
    --filename=green_tripdata_2019-09.csv

python ./scripts/load_taxi_data.py\
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db=ny_taxi \
    --table_name=taxi_zones \
    --url="https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv" \
    --filename=taxi_zone_lookup.csv