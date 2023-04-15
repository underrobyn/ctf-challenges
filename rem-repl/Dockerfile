FROM php:8.2.4-cli-alpine

RUN apk update && apk add --no-cache bash git rlwrap readline-dev nmap-ncat

# Install PHP extensions
COPY --from=mlocati/php-extension-installer /usr/bin/install-php-extensions /usr/local/bin/
RUN install-php-extensions pcntl pdo_sqlite posix readline sodium

COPY server.sh /tmp/server.sh

# Copy settings to make environment more secure
COPY extra.ini /usr/local/etc/php/conf.d/extra.ini

WORKDIR /app

# Expose the port that will be forwarded to the host
EXPOSE 2222

# Start the container in the background
CMD ["bash", "-c", "/tmp/server.sh"]

