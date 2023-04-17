#!/bin/bash

docker build -t rctf_rem_serveradmin .

docker container rm rctf_serveradmin_app

docker run \
    -p 5555:5555 \
    --name rctf_serveradmin_app \
    rctf_rem_serveradmin
