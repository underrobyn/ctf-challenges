#!/bin/bash

docker build -t rctf_for_encryptproject .

docker container rm rctf_encryptproject_app

docker run \
    -v out:/data \
    --name rctf_encryptproject_app \
    rctf_for_encryptproject

docker cp rctf_encryptproject_app:/jar/CCEncryptService.jar .
