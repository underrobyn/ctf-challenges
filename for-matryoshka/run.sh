#!/bin/bash

docker build -t rctf_for_matroshka .

docker run \
    --rm \
    --it \
    -v $(pwd):/data
    --name rctf_matroshka_gen \
    rctf_for_matroshka
