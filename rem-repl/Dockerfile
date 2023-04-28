FROM php:8.2.5-cli-alpine3.17

RUN apk update && apk add --no-cache bash git rlwrap readline-dev nmap-ncat

# Install PHP extensions
COPY --from=mlocati/php-extension-installer /usr/bin/install-php-extensions /usr/local/bin/
RUN install-php-extensions pcntl pdo_sqlite posix readline sodium

COPY server.sh /tmp/server.sh

# Copy settings to make environment more secure
COPY conf.d/secure-env.ini /usr/local/etc/php/conf.d/secure-env.ini

# Copy flag to a random file name :)
COPY flag1.txt /flag.txt
RUN mv /flag.txt /flag_$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 15 | head -n 1).txt

COPY flag2.txt /tmp/flag2.txt
RUN echo "export FLAG2=$(cat /tmp/flag2.txt)" >> /root/.bashrc
RUN rm -f /tmp/flag2.txt

WORKDIR /app

# Expose the port that will be forwarded to the host
EXPOSE 2222

# Start the container in the background
CMD ["bash", "-c", "/tmp/server.sh"]

