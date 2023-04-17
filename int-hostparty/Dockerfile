FROM ubuntu:jammy-20230308

RUN apt-get update && \
    apt-get install -y cron python vsftpd && \
    rm -rf /var/lib/apt/lists/*

# Configure the FTP server
RUN echo "anonymous_enable=YES" >> /etc/vsftpd.conf && \
    echo "anon_root=/srv/ftp" >> /etc/vsftpd.conf && \
    echo "local_enable=NO" >> /etc/vsftpd.conf && \
    echo "write_enable=NO" >> /etc/vsftpd.conf && \
    echo "anon_upload_enable=NO" >> /etc/vsftpd.conf && \
    echo "anon_mkdir_write_enable=NO" >> /etc/vsftpd.conf

RUN mkdir -p /srv/ftp && \
    touch /srv/ftp/info.txt && \
    chmod 777 /srv/ftp && \
    chmod 444 /srv/ftp/info.txt

RUN mkdir -p /srv/ftp/{logs,tmp,secret}

COPY ./ftproot/logs/* /srv/ftp/logs/
COPY ./ftproot/tmp/* /srv/ftp/tmp/

# Configure the automated population script
RUN (crontab -l 2>/dev/null; echo "* * * * * python3 /root/randomly-populate.py") | crontab -
RUN (crontab -l 2>/dev/null; echo "* * * * * python3 /root/randomly-populate.py") | crontab -

EXPOSE 20 21

CMD ["/usr/sbin/vsftpd", "/etc/vsftpd.conf"]
