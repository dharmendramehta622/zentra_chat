#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate
 
# Set environment variables
export DJANGO_SUPERUSER_USERNAME="zentra_admin"
export DJANGO_SUPERUSER_PASSWORD="CRACE4DOJ309#esf"
export DJANGO_SUPERUSER_EMAIL="admin@zentra.com"  # Make sure to set this value

# DJANGO_SUPERUSER_USERNAME=$SUPERUSER_USERNAME \
#     DJANGO_SUPERUSER_PASSWORD=$SUPERUSER_PASSWORD \
#     python3 manage.py createsuperuser \
#     --noinput \
#     --email $SUPERUSER_EMAIL 

# Use the createsuperuser management command with environment variables
python3 manage.py createcustomsuperuser

# Run the Development Server
# python3 manage.py runserver 0.0.0.0:8000


# Run the ASGI server using Uvicorn
uvicorn zentra_chat.asgi:application --host 0.0.0.0 --port 8000
# daphne  -p 8000 zentra_chat.asgi:application
# gunicorn -w 4 -b 0.0.0.0:8000 main:app

