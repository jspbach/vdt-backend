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

if [ "$USE_FIXTURES" = "true" ]
then
  echo "Populate database with fixtures..."
  python manage.py loaddata members/fixtures/mock_members.json
else
  echo "USE_FIXTURES is not set to true, skipping fixture population."
fi


exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 apiserver.wsgi:application
