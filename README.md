a simple app to demonstrate celery tasks, periodic tasks and django.

# Development Quick Start

## Development Webserver
``` terminal
python manage.py runserver
```

## Development Celery
``` terminal
celery -A pjapp worker -l debug --concurrency 1
```
