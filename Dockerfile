FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /my_app
WORKDIR /my_app

COPY requirements.txt /my_app/
RUN pip install -r requirements.txt
COPY . /my_app/

RUN chmod +x run.sh