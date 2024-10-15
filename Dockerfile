FROM python:3.10-slim

LABEL maintainer="denys.piuro@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

# Install all dependencies
RUN pip install -r requirements.txt

COPY . .

RUN adduser \
      --disabled-password \
      --no-create-home \
      django-user

RUN mkdir -p /vol/web/media
RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
