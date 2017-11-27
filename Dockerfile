FROM python:3-alpine


WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt