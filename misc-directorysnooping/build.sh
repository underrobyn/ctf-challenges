#!/bin/bash

docker build -t rctf_misc_directorysnooping .

docker image tag rctf_misc_directorysnooping robynctf.azurecr.io/misc_directorysnooping

docker image push robynctf.azurecr.io/misc_directorysnooping
