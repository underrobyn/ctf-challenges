#!/bin/bash

docker build -t rctf_int_lookclosely .

docker run \
    -p 8080:8080 \
    --name rctf_lookclosely_app \
    rctf_int_lookclosely
