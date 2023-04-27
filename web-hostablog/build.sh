#!/bin/bash

docker build -t rctf_web_hostablog .

docker image tag rctf_web_hostablog robynctf.azurecr.io/web_hostablog

docker image push robynctf.azurecr.io/web_hostablog
