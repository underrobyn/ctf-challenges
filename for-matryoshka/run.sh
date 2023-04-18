#!/bin/bash

docker build -t rctf_for_matroshka .

docker run \
    -it \
    -v data:/mnt/data \
    --name rctf_matroshka_gen \
    rctf_for_matroshka
