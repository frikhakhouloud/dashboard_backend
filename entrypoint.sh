#!/bin/bash
whoami
mkdir -p /media || true
chmod -R 777 /media
PGPASSWORD=$PG_PASSWORD PGHOST=$PG_HOST psql -U $PG_USER -c "CREATE DATABASE dashboard_db;" || true
PGPASSWORD=$PG_PASSWORD PGHOST=$PG_HOST psql -U $PG_USER -c "GRANT ALL PRIVILEGES ON DATABASE dashboard_db TO postgres;" || true

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000 --noreload