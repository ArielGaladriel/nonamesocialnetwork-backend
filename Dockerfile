FROM python:3.10.5

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt && pip install django-environ
RUN sed -i 's/from django.utils.http import urlquote/from urllib.parse import quote as urlquote/' /usr/local/lib/python3.10/site-packages/social_django/middleware.py

COPY . /usr/src/app