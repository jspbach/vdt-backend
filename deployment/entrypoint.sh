#!/bin/bash
cd apiserver/

# Check if RERUN_MIGRATIONS is set to true
if [ "$RERUN_MIGRATIONS" = "true" ]
then
  echo "Running migrations..."
  python manage.py makemigrations members
  python manage.py migrate members
else
  echo "RERUN_MIGRATIONS is not set to true, skipping migrations."
fi

exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 apiserver.wsgi:application