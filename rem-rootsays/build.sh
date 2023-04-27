#!/bin/bash

docker build -t rctf_rem_rootsays .

docker image tag rctf_rem_rootsays robynctf.azurecr.io/rem_rootsays

docker image push robynctf.azurecr.io/rem_rootsays
