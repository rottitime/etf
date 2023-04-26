#!/bin/sh

set -o errexit
set -o nounset

# Copy across generated files to local docker-compose volume
cp -R /output/* /app/static/dist/

python manage.py migrate --noinput
watchmedo auto-restart --directory=./  --pattern=""*.py"" --recursive -- waitress-serve --port=$PORT --threads=8 etf.wsgi:application
