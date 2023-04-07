FROM python:3.11.3-slim-bullseye

RUN apt-get update && \
    apt-get -qy full-upgrade && \
    apt-get install -qy curl python3 && \
    curl -sSL https://get.docker.com/ | sh
