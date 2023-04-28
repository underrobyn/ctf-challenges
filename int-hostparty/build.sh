#!/bin/bash

docker build -t rctf_int_hostparty .

docker image tag rctf_int_hostparty robynctf.azurecr.io/int_hostparty

docker image push robynctf.azurecr.io/int_hostparty
