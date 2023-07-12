FROM python:3.10.12-bookworm
USER root
COPY manage.py /
COPY dash /dash
COPY filtre /filtre
COPY order_past /order_past
COPY requirements.txt /requirements.txt
RUN  pip install -r /requirements.txt
RUN apt update
RUN apt install -y postgresql-client
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]





