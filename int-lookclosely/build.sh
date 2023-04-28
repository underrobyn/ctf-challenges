#!/bin/bash

docker build -t rctf_int_lookclosely .

docker image tag rctf_int_lookclosely robynctf.azurecr.io/int_lookclosely

docker image push robynctf.azurecr.io/int_lookclosely
