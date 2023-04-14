#!/bin/bash

docker build -t rctf_rem_psysh .

docker container rm rctf_psysh_app

docker run \
    -p 2222:2222 \
    --name rctf_psysh_app \
    rctf_rem_psysh
