#!/bin/bash

docker-compose up -d --build
docker-compose run tools python3 populate_db.py 100000
