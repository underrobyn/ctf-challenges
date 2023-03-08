FROM python:3.11-slim-bullseye

ARG UNAME=appuser
ARG UID=1000

WORKDIR /code

RUN apt-get update

RUN useradd $UNAME -u $UID --system

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

USER $UNAME

COPY --chown=$UID:$UID ./flag.txt /tmp/flag.txt
COPY --chown=$UID:$UID ./app /code/app/

# If running behind a proxy like Nginx or Traefik add --proxy-headers
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]