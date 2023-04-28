#!/bin/bash

docker build -t rctf_misc_jeffrey .

docker run \
    --rm \
    --env-file .env \
    -p 5000:5000 \
    --name rctf_jeffrey_app \
    rctf_misc_jeffrey
