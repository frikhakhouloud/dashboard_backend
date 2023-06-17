#!/bin/bash
whoami
mkdir -p /media || true
chmod -R 777 /media
PGPASSWORD=$PG_PASSWORD PGHOST=$PG_HOST psql -U $PG_USER -c "CREATE DATABASE dashboard_db;" || true
PGPASSWORD=$PG_PASSWORD PGHOST=$PG_HOST psql -U $PG_USER -c "GRANT ALL PRIVILEGES ON DATABASE dashboard_db TO postgres;" || true

python manage.py makemigrations
python manage.py migrate

#pbkdf2_sha256$390000$otpWruZLf1FEoE9z7vAiJ6$+eXnAFCRDpaQ7YUpeHTEnfmzfHBIWABmn/KyVVJXzOM=

PGPASSWORD=$PG_PASSWORD PGHOST=$PG_HOST psql -U $PG_USER -c "INSERT INTO public.auth_user(password,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined) VALUES ('','1','khouloud','frikha','khouloud','khouloud@gmail.com','1','1','2023-04-30');" || true

python manage.py runserver 0.0.0.0:8000 --noreload