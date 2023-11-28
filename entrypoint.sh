#!/bin/sh

# Wait for PostgreSQL to be ready
while ! nc -z db 5432; do
  sleep 0.1
done

# Apply migrations
python manage.py migrate

# Start the Django development server
python manage.py runserver 0.0.0.0:8000