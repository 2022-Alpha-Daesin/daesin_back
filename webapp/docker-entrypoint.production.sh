#!/bin/bash
python ./manage.py makemigrations --noinput

python manage.py migrate --noinput

python manage.py collectstatic --noinput

gunicorn config.wsgi:application --bind 0.0.0.0:8000