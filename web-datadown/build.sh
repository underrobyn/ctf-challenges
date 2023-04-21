#!/bin/bash

docker build -t rctf_web_datadown .

docker image tag rctf_web_datadown robynctf.azurecr.io/web_datadown

docker image push robynctf.azurecr.io/web_datadown
