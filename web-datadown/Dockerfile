FROM php:8.1-apache-bullseye

USER root

RUN apt-get update && apt-get install -y git unzip

# Install PHP extensions
COPY --from=mlocati/php-extension-installer /usr/bin/install-php-extensions /usr/local/bin/
RUN install-php-extensions pdo_mysql pdo_sqlite sodium

# Set hostname for development
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Switch to local user
USER www-data

# Copy source to html folder
COPY src/ /var/www/html/
COPY flag.txt /flag.txt

# Set workdir as ./web
WORKDIR /var/www/html

# Create database
RUN php create-database.php

EXPOSE 80
