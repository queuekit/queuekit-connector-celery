from celery import Celery
import os


def get_celery_app(broker_url, backend_url):
    app = Celery('celery_connector', broker=broker_url, backend=backend_url)

    return app
