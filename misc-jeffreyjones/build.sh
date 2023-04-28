#!/bin/bash

docker build -t rctf_misc_jeffrey .

docker image tag rctf_misc_jeffrey robynctf.azurecr.io/misc_jeffrey

docker image push robynctf.azurecr.io/misc_jeffrey
