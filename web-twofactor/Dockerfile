FROM python:3.11.3-alpine3.17

ARG USER=app

WORKDIR /tmp

RUN apk update && \
    apk add --no-cache --virtual .build-deps build-base && \
    addgroup -g 1000 -S $USER && \
    adduser -u 1000 -S $USER -G $USER && \
    python -m pip install pip==23.0.1

COPY --chown=$USER:$USER requirements.txt .

RUN python -m pip install -r requirements.txt

RUN mkdir -p /app && chown -R $USER:$USER /app

WORKDIR /app

USER $USER

COPY --chown=$USER:$USER ./src .

EXPOSE 5000

CMD ["/bin/sh", "-c", "/app/wsgi.sh"]
