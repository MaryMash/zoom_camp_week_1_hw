FROM python:3.10-alpine

WORKDIR /app

RUN pip install --upgrade pip && pip install pandas sqlalchemy psycopg2-binary

COPY scripts scripts

RUN chmod +x scripts/run_all.sh

ENTRYPOINT [ "./scripts/run_all.sh" ]