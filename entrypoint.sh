#!/bin/bash

set -e

until python manage.py makemigrations
do
    echo "Waiting for db to be ready..."
    sleep 5
done

echo "${0}: applying migrations."
python manage.py migrate --noinput

echo "${0}: collecting static files."
python manage.py collectstatic --noinput


# echo server starting
echo "${0}: starting server."

python manage.py runserver 0.0.0.0:8000