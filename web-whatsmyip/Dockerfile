FROM php:8.2.5-apache-bullseye

USER root

RUN apt-get update && apt-get install -y bind9-utils ca-certificates dnsutils inet-utils-ping net-tools

# Set hostname for development
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Copy source to html folder
COPY src/ /var/www/html/
COPY flag.txt /flag.txt

# Set workdir as ./web
WORKDIR /var/www/html

# Switch to local user
USER www-data

EXPOSE 80
