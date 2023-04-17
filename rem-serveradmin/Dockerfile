FROM ubuntu:jammy-20230308

ARG UNAME=user
ARG UPWD=Password123
ARG UID=1000
ARG GID=1000

RUN apt-get update && \
    apt-get -qy full-upgrade

RUN apt-get install -y sudo htop ncat net-tools openssl openssh-server

COPY provision.sh /tmp/provision.sh

# Provision users
RUN groupadd -g $GID fred && \
    useradd $UNAME -u $UID -g $GID --create-home -s /bin/bash && \
    echo "$UNAME:$UPWD" | chpasswd && \
    /tmp/provision.sh && \
    rm -f /tmp/provision.sh

# Fix SSH server
RUN mkdir /run/sshd && \
    chmod 0755 /run/sshd

# Copy flag
COPY flag.txt /flag.txt

RUN mv /flag.txt /home/jimmy/folder1/flag_$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 15 | head -n 1).txt
RUN chmod 600 /home/jimmy/folder1/flag_*.txt

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
