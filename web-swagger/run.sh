#!/bin/bash

docker build -t rctf_web_swagger .

docker container rm rctf_webswagger_app

docker run \
    -p 8080:80 \
    --env DATABASE_URI='sqlite:////tmp/app.db' \
    --name rctf_webswagger_app \
    rctf_web_swagger
