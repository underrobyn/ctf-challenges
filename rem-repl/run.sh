#!/bin/bash

docker build -t rctf_rem_repl .

docker container rm rctf_repl_app

docker run \
    -p 2222:2222 \
    --name rctf_repl_app \
    rctf_rem_repl
