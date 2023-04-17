FROM ubuntu:jammy-20230308

ARG UNAME=user
ARG UID=1000
ARG GID=1000

RUN apt-get update && \
    apt-get -qy full-upgrade && \
    apt-get install -y sudo vim htop net-tools openssl ncat

RUN groupadd -g $GID fred && \
    useradd $UNAME -u $UID -g $GID --create-home -s /bin/bash && \
    echo "alias ll='ls -Fail'" >> .bashrc && \
    echo "usr ALL=(ALL) NOPASSWD: /usr/bin/sudo -l" >> /etc/sudoers && \
    echo "usr ALL=(ALL) NOPASSWD: /usr/bin/local/python" >> /etc/sudoers

COPY provision.sh /tmp/provision.sh
COPY server.sh /tmp/server.sh

RUN /tmp/provision.sh && rm -f /tmp/provision.sh

WORKDIR /home/user

COPY flag.txt /home/jimmy/folder1/flag.txt

RUN chmod 600 /home/jimmy/folder1/flag.txt

USER $UNAME

EXPOSE 5555

CMD ["/tmp/server.sh"]
