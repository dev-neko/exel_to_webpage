web: gunicorn config.wsgi
worker: celery worker -A config -l INFO --pool=solo --loglevel=INFO