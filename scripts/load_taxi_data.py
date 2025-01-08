import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    filename = params.filename

    # os.system(f"curl -LfO {url}")

    os.system(f"wget {url}")
    if "tripdata" in filename:
        os.system(f'gzip -d {filename}.gz')

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    df_iter = pd.read_csv(filename, iterator=True, chunksize=100000)
    df = next(df_iter)

    if "tripdata" in filename:
        df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
        df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists="append")
    df.to_sql(name=table_name, con=engine, if_exists="append")

    while True:
        t_start = time()
        df = next(df_iter)
        if "tripdata" in filename:
            df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
            df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
        df.to_sql(name=table_name, con=engine, if_exists="append")
        t_end = time()
        print(f"inserted another chunk, time spent: {t_end - t_start}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')
    parser.add_argument('--filename', help='name of the csv file')
    args = parser.parse_args()

    main(args)