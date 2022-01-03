#!/bin/bash

docker-compose run tools pgloader mysql://user:password@mysql/database postgresql://postgres:password@postgres/database
