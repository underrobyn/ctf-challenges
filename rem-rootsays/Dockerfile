FROM ubuntu:jammy-20230308

ARG UNAME=user
ARG UID=1000
ARG GID=1000

RUN apt-get update && \
    apt-get -qy full-upgrade && \
    apt-get install -y sudo ncat

RUN groupadd -g $GID simon && \
    useradd $UNAME -u $UID -g $GID --create-home -s /bin/bash && \
    echo "ALL ALL=(ALL) NOPASSWD:/usr/bin/sudo -l" >> /etc/sudoers && \
    echo "user ALL=(ALL) NOPASSWD:/bin/cat" >> /etc/sudoers

COPY flag.txt /flag.txt
RUN mv /flag.txt /flag_$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 15 | head -n 1).txt && \
    chmod -R 600 /flag_*.txt

WORKDIR /home/$UNAME

USER $UNAME

COPY server.sh /tmp/server.sh

EXPOSE 5555

CMD ["bash", "-c", "/tmp/server.sh"]
