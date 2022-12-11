#!/bin/bash
python ./manage.py makemigrations --noinput --settings=config.settings.prod

python manage.py migrate --noinput --settings=config.settings.prod

python manage.py pull_major --settings=config.settings.prod
python manage.py pull_menus --settings=config.settings.prod
python manage.py init_tags --settings=config.settings.prod
python manage.py init_club --settings=config.settings.prod
python manage.py collectstatic --noinput --settings=config.settings.prod

gunicorn config.wsgi:application --env DJANGO_SETTINGS_MODULE=config.settings.prod --bind 0.0.0.0:8000