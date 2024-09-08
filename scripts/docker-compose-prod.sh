#!/bin/sh

cd ..
sudo docker compose -f ./docker/docker-compose-prod.yml up -d
