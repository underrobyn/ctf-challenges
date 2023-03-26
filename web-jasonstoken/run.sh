#!/bin/bash

docker build -t rctf_web_jasonstoken .

docker container rm rctf_jasonstoken_app

docker run \
    -p 8080:3000 \
    --name rctf_jasonstoken_app \
    rctf_web_jasonstoken
