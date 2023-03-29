#!/bin/bash

docker build -t rctf_rem_ncserver .

docker container rm rctf_ncserver_app

docker run \
    -p 5555:5555 \
    --name rctf_ncserver_app \
    rctf_rem_ncserver
