#!/bin/sh

set -e

until python manage.py migrate; do
  echo "Migration problems, possibly DB server is unavailable"
  sleep 5
done

python manage.py runserver 0.0.0.0:8000
