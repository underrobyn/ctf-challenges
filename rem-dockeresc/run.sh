#!/bin/bash

docker build -t rctf_rem_dockeresc .

docker container rm rctf_dockeresc_app

docker run \
  -p 5555:5555 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --name rctf_dockeresc_app \
  rctf_rem_dockeresc
