FROM python:3.11.3-alpine3.17

ARG UNAME=appuser
ARG UID=1000

WORKDIR /code

RUN adduser $UNAME -u $UID -S

RUN apk add git

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

USER $UNAME

# Copy the app code
COPY --chown=$UID:$UID ./app /code/app/

EXPOSE 5000

# If running behind a proxy like Nginx or Traefik add --proxy-headers
CMD ["gunicorn", "app.app:app", "--bind=0.0.0.0:5000", "--workers=4"]
