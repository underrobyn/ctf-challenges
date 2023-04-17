#!/bin/bash

docker build -t rctf_rem_rootsays .

docker container rm rctf_rootsays_app

docker run \
  -p 5555:5555 \
  --name rctf_rootsays_app \
  rctf_rem_rootsays
