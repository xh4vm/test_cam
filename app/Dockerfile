FROM python:3.11-slim AS builder

WORKDIR /opt
COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends build-essential python3-dev gcc musl-dev libc-dev \
     && pip install --upgrade pip \
     && pip3 install wheel && pip3 wheel -r requirements.txt --wheel-dir=/opt/wheels


FROM python:3.11-slim

COPY --from=builder /opt /opt

WORKDIR /opt/app
EXPOSE ${APP_PORT}
ENTRYPOINT ["uwsgi", "--strict", "--ini", "uwsgi.ini"]

COPY . .
RUN  mkdir -p /var/www/static/ && pip install --no-index --find-links=/opt/wheels -r requirements.txt