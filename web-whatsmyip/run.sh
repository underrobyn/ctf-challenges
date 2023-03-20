#!/bin/bash

docker build -t rctf_web_whatsmyip .

docker container rm rctf_whatsmyip_app

docker run \
    -p 8080:80 \
    --name rctf_whatsmyip_app \
    rctf_web_whatsmyip
