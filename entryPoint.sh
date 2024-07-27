#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate
 
# Set environment variables
export SUPERUSER_USERNAME="playground_admin"
export SUPERUSER_PASSWORD="CRACE4DOJ309#esf"
export SUPERUSER_EMAIL="admin@playground.com"  # Make sure to set this value

DJANGO_SUPERUSER_USERNAME=$SUPERUSER_USERNAME \
    DJANGO_SUPERUSER_PASSWORD=$SUPERUSER_PASSWORD \
    python3 manage.py createsuperuser \
    --noinput \
    --email $SUPERUSER_EMAIL 

python3 manage.py runserver 0.0.0.0:8000
# daphne -b 0.0.0.0 -p 8000 home_automation.asgi:application
# gunicorn -w 4 -b 0.0.0.0:8000 main:app

