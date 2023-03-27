FROM ubuntu:jammy

ARG UNAME=user
ARG UID=1000
ARG GID=1000

RUN apt-get update && \
    apt-get -qy full-upgrade && \
    apt-get install -y sudo ncat

RUN groupadd -g $GID filelock && \
    useradd $UNAME -u $UID -g $GID --create-home -s /bin/bash && \
    echo "alias ll='ls -Fail'" >> .bashrc && \
    echo "usr ALL=(ALL) NOPASSWD: /usr/bin/sudo -l" >> /etc/sudoers

WORKDIR /opt/myapp

COPY server.sh /tmp/server.sh

USER $UNAME

EXPOSE 5555

CMD ["/tmp/server.sh"]
