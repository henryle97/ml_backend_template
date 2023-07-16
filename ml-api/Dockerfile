FROM python:3.9.5-slim-buster

# Maintainer
LABEL maintainer="Henry"

# Set working directory
WORKDIR /app

# Environment variables 
## disables the generation of .pyc files
ENV PYTHONDONTWRITEBYTECODE 1 
## disables Python's output buffering
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN pip instal --upgrade pip 

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


COPY ./app/ /app/ 
