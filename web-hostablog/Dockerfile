FROM php:latest

RUN useradd www -d /code -s /usr/sbin/nologin

RUN mkdir -p /code && chown -R www:www /code

WORKDIR /code

USER www

EXPOSE 80