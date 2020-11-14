FROM snakepacker/python:all as builder
MAINTAINER vnkrtv

COPY requirements.txt /mnt/

RUN python3.7 -m venv /usr/share/python3/venv \
 && /usr/share/python3/venv/bin/pip install -U pip \
 && /usr/share/python3/venv/bin/pip install -Ur /mnt/requirements.txt

FROM snakepacker/python:3.7 as base

COPY --from=builder /usr/share/python3/venv /usr/share/python3/venv
COPY . /usr/share/python3/

RUN . /usr/share/python3/venv/bin/activate \
 && cd /usr/share/python3/
ENTRYPOINT ["gunicorn wsgi:app -b 0.0.0.0:8000"]