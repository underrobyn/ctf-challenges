#!/bin/bash

docker build -t rctf_rem_serveradmin .

docker image tag rctf_rem_serveradmin robynctf.azurecr.io/rem_serveradmin

docker image push robynctf.azurecr.io/rem_serveradmin
