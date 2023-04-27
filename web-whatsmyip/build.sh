#!/bin/bash

docker build -t rctf_web_whatsmyip .

docker image tag rctf_web_whatsmyip robynctf.azurecr.io/web_whatsmyip

docker image push robynctf.azurecr.io/web_whatsmyip
