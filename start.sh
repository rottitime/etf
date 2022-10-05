#!/bin/sh

set -o errexit
set -o nounset

python manage.py migrate --noinput
watchmedo auto-restart --directory=./  --pattern=""*.py"" --recursive -- waitress-serve --port=$PORT business_case_approval.wsgi:application
