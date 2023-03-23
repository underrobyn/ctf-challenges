#!/bin/bash

docker build -t rctf_web_twofactor .

docker container rm rctf_twofactor_app

docker run \
    -p 5000:5000 \
    --name rctf_twofactor_app \
    rctf_web_twofactor
