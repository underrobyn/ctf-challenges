#!/bin/bash

docker build -t rctf_int_hostparty .

docker run \
    -p 20:20 \
    -p 21:21 \
    --name rctf_int_hostparty_app \
    rctf_int_hostparty
