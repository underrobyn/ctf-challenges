FROM python:3.11.2-slim-bullseye

ARG DATABASE_URI='sqlite:////tmp/app.db'
ARG UNAME=appuser
ARG UID=1000

WORKDIR /code

RUN apt-get update

RUN useradd $UNAME -u $UID --system

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

USER $UNAME

# Copy the flags
COPY --chown=$UID:$UID ./flag1.txt /flag_user.txt
COPY --chown=$UID:$UID ./flag2.txt /flag_admin.txt

# Copy the app code
COPY --chown=$UID:$UID ./app /code/app/

RUN python ./app/setup.py

# If running behind a proxy like Nginx or Traefik add --proxy-headers
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]
