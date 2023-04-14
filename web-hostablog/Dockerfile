FROM php:8.2.4-apache-bullseye

USER root

# Set hostname for development
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Copy source to html folder
COPY src/ /var/www/html/
COPY flag.txt /flag.txt

WORKDIR /var/www/html

# Switch to local user
USER www-data

EXPOSE 80
