#!/bin/bash

docker build -t rctf_web_datadown .

docker container rm rctf_datadown_app

docker run \
    -p 8080:80 \
    --name rctf_datadown_app \
    rctf_web_datadown
