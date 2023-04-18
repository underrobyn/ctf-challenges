FROM ubuntu:jammy-20230308

RUN apt-get update && \
    apt-get install -y bash cron python3 vsftpd && \
    rm -rf /var/lib/apt/lists/*

# Configure the FTP server
COPY ./vsftpd.conf /etc/vsftpd.conf

RUN mkdir -p /srv/ftp && \
    touch /srv/ftp/info.txt && \
    chmod 777 /srv/ftp && \
    mkdir -p /var/run/vsftpd/empty && \
    chmod a-w /var/run/vsftpd && \
    chmod a-w /var/run/vsftpd/empty

RUN mkdir -p /srv/ftp/logs && \
    mkdir -p /srv/ftp/secret && \
    mkdir -p /srv/ftp/tmp

COPY ./ftproot/logs/* /srv/ftp/logs/
COPY ./ftproot/tmp/* /srv/ftp/tmp/
COPY ./scripts/* /root/

# Configure the automated population script
RUN (crontab -l 2>/dev/null; echo "* * * * * /bin/bash /root/tmp.sh") | crontab -
RUN service cron start

# Run initial
RUN /usr/bin/python3 /root/randomly-populate.py && \
    chown -R nobody:nogroup /srv/ftp && \
    chmod -R 444 /srv/ftp && \
    chmod -R 777 /srv/ftp/tmp

EXPOSE 20 21 50000-50009

CMD ["/usr/sbin/vsftpd", "/etc/vsftpd.conf"]
