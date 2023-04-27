#!/bin/bash

docker build -t rctf_web_swagger .

docker image tag rctf_web_swagger robynctf.azurecr.io/web_swagger

docker image push robynctf.azurecr.io/web_swagger
