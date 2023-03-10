#!/bin/bash

docker build -t rctf_inf_lookclosely .

docker run \
    -p 8080:8080 \
    --name rctf_lookclosely_app \
    rctf_inf_lookclosely
