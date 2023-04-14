FROM php:8.2.4-cli-alpine

RUN apk update && apk add --no-cache bash git rlwrap readline-dev nmap-ncat

# Install PHP extensions
COPY --from=mlocati/php-extension-installer /usr/bin/install-php-extensions /usr/local/bin/
RUN install-php-extensions pcntl pdo_sqlite posix readline sodium

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install PsySH
RUN composer global require psy/psysh:@stable
COPY config.php /root/.config/psysh/config.php
COPY server.sh /tmp/server.sh

# Set the path to the PsySH binary
ENV PATH="/root/.composer/vendor/bin:${PATH}"

WORKDIR /app

# Expose the port that will be forwarded to the host
EXPOSE 2222

# Start the container in the background
# CMD ["sh", "-c", "psysh --config /root/.config/psysh/config.php > /dev/null & tail -f /dev/null"]
CMD ["bash", "-c", "/tmp/server.sh"]

