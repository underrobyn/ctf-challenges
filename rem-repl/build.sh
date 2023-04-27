#!/bin/bash

docker build -t rctf_rem_repl .

docker image tag rctf_rem_repl robynctf.azurecr.io/rem_repl

docker image push robynctf.azurecr.io/rem_repl
