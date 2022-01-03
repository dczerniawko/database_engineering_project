FROM debian:bullseye

RUN apt-get update && apt-get install -y \
    libmariadb-dev-compat \
    mariadb-client \
    pgloader \
    postgresql-client \
    python3-pip
RUN pip install \
    faker \
    mysqlclient \
    pandas \
    sqlalchemy

WORKDIR /file
COPY populate_db.py populate_db.py
