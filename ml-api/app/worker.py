from redis import Redis
from celery import Celery
from app.configs import settings


redis = Redis()
celery_execute = Celery()