#!/bin/bash
PGPASSWORD=$PG_PASSWORD PGHOST=$PG_HOST psql -U $PG_USER -c "CREATE DATABASE dashboard_db;" || true
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000 --noreload