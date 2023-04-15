#!/bin/bash

while true; do
  echo nc starting
  ncat -nvl -p 2222 -c "rlwrap php -a"
done
