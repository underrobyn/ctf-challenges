#!/bin/bash

docker build -t rctf_for_sharkinthewires.

docker container rm rctf_sharkinthewires_app

docker run \
    -p 23:23 \
    --name rctf_sharkinthewires_app \
    rctf_for_sharkinthewires
