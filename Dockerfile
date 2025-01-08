FROM python:3.10-alpine

WORKDIR /app

RUN pip install --upgrade pip && pip install pandas sqlalchemy psycopg2-binary

COPY scripts scripts

RUN chmod +x scripts/run_all.sh

ENTRYPOINT [ "./scripts/run_all.sh" ]

#ENTRYPOINT [ "python", "load_taxi_data.py" ]
#
#CMD ["--user", "root", "--password", "root", "--host", "pgdatabase", "--port", "5432", "--db", "ny_taxi", "--table_name", "green_taxi_data", "--url", "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz", "--filename", "green_tripdata_2019-09.csv"]