#!/bin/bash
python manage.py makemigrations --noinput

python manage.py migrate --noinput

python manage.py collectstatic --noinput

python manage.py runserver --settings=config.settings.base 0.0.0.0:8000