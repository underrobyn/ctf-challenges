FROM ubuntu:jammy-20230308

ARG UNAME=user
ARG UPWD=WeAllWalkAloneOnAnEmptyStaircase8111
ARG UID=1000
ARG GID=1000

RUN apt-get update && \
    apt-get -qy full-upgrade

RUN apt-get install -y net-tools openssl xinetd telnetd sudo vim

# Create telnet service configuration
RUN echo "service telnet\n\
{\n\
        disable         = no\n\
        flags           = REUSE\n\
        socket_type     = stream\n\
        wait            = no\n\
        user            = root\n\
        server          = /usr/sbin/in.telnetd\n\
        server_args     = -L /bin/login\n\
        log_on_failure  += USERID\n\
}" > /etc/xinetd.d/telnet

# Provision users
RUN groupadd -g $GID $UNAME && \
    useradd $UNAME -u $UID -g $GID --create-home -s /bin/bash && \
    echo "$UNAME:$UPWD" | chpasswd

# Expose telnet port
EXPOSE 23

# Start xinetd in foreground
CMD ["xinetd", "-dontfork"]
