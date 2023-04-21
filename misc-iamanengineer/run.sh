#!/bin/bash

docker build -t rctf_misc_jeffrey .

docker image tag rctf_misc_jeffrey robynctf.acr.io/misc_jeffrey

docker run \
    --rm \
    -p 5000:5000 \
    --name rctf_jeffrey_app \
    rctf_misc_jeffrey
