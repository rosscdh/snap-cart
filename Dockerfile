FROM python:3-alpine


WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt