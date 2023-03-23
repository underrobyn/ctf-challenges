#!/bin/sh

gunicorn --bind=0.0.0.0:5000 --workers=1 --preload -c /app/config.py app:app
