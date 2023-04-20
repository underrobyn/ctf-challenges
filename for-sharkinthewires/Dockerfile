FROM ubuntu:jammy-20230308

ARG UNAME=user
ARG UPWD=WeAllWalkAloneOnAnEmptyStaircase8111
ARG UID=1000
ARG GID=1000

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y telnetd xinetd net-tools openssl sudo vim

# Create a configuration file for the Telnet server
RUN echo "service telnet\n{\nflags = REUSE\nsocket_type = stream\nwait = no\nuser = root\nserver = /usr/sbin/in.telnetd\nlog_on_failure += USERID\ndisable = no\n}\n" > /etc/xinetd.d/telnet

# Provision users
RUN groupadd -g $GID $UNAME && \
    useradd $UNAME -u $UID -g $GID --create-home -s /bin/bash && \
    echo "$UNAME:$UPWD" | chpasswd && \
    echo "ALL ALL=(ALL) NOPASSWD:/usr/bin/sudo -l" >> /etc/sudoers && \
    echo "user ALL=(ALL) NOPASSWD:/bin/cat" >> /etc/sudoers && \
    echo "user ALL=(ALL) NOPASSWD:/bin/rm" >> /etc/sudoers

RUN echo "flag{43ncrypt_y0ur_tr4ff1c__3v3n_1nt3rn41}" >> /flag.txt

EXPOSE 23

# Start the xinetd service to enable the Telnet server
CMD ["/usr/sbin/xinetd", "-dontfork"]
