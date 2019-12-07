#!/bin/sh
python manage.py runserver_plus --key-file credentials/private_key.pem --cert-file credentials/server.pem
# gunicorn --certfile=credentials/server.pem --keyfile=credentials/private_key.pem speechclassification.wsgi

