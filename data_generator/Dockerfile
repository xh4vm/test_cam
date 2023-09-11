FROM python:3.11-slim as data_generator-builder

WORKDIR /opt
COPY requirements.txt ./

RUN  apt-get update \
     && pip install --upgrade pip \
     && pip install wheel && pip3 wheel -r requirements.txt --wheel-dir=/opt/wheels


FROM python:3.11-slim

COPY --from=data_generator-builder /opt /opt

WORKDIR /opt/data_generator

COPY . .
RUN pip install --no-index --find-links=/opt/wheels -r requirements.txt