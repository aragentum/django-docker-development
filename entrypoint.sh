#!/bin/bash

set -e

until poetry python manage.py migrate; do
  echo "Migration problems, possibly DB server is unavailable"
  sleep 5
done

poetry python manage.py runserver 0.0.0.0:8000
