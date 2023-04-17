#!/bin/bash

docker build -t rctf_int_hostparty .

docker run \
    -p 20:20 \
    -p 21:21 \
    -p 50000-50009:50000-50009 \
    --name rctf_int_hostparty_app \
    rctf_int_hostparty
