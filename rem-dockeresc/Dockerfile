FROM ubuntu:jammy-20230308

RUN apt-get update && \
    apt-get -qy full-upgrade && \
    apt-get install -qy apt-transport-https apt-utils bash ca-certificates curl python3 wget

RUN curl -sSL https://get.docker.com/ | sh

CMD ["bash"]
