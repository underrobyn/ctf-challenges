FROM python:3.11.3-slim-bullseye

ARG UNAME=user
ARG UID=1000
ARG GID=1001

RUN apt-get update && \
    apt-get -qy full-upgrade && \
    apt-get install sudo

RUN groupadd -g $GID filelock && \
    useradd $UNAME -u $UID -g $GID --create-home -s /bin/bash && \
    echo "alias ll='ls -Fail'" >> .bashrc && \
    echo "usr ALL=(ALL) NOPASSWD: /usr/bin/sudo -l" >> /etc/sudoers && \
    echo "usr ALL=(ALL) NOPASSWD: /usr/bin/local/python" >> /etc/sudoers

WORKDIR /opt/myapp

COPY flag.txt /opt/myapp/flag.txt
COPY reader.py /opt/myapp/reader.py

RUN chmod 600 /opt/myapp/flag.txt && chmod 644 /opt/myapp/reader.py

USER $UNAME

CMD ["bash"]
