#!/bin/bash

docker build -t rctf_web_hostablog .

docker container rm rctf_hostablog_app

docker run \
    -p 8080:80 \
    --name rctf_hostablog_app \
    rctf_web_hostablog
