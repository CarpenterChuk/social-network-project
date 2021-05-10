FROM python:3.7-alpine
MAINTAINER Vladyslav Stoliarchuk

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /devgram
WORKDIR /devgram
COPY ./devgram /devgram

RUN adduser -D user

USER user