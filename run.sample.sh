#!/bin/sh

# python manage.py
# Donni Richasdy Certificate
python manage.py runserver_plus --key-file credentials/private_key.pem --cert-file credentials/server.pem

# *.localhost/CN=localhost
# Dummy Certificate
python manage.py runserver_plus --key-file credentials/server.key --cert-file credentials/server.crt
python manage.py runserver_plus --key-file credentials/private_key.key --cert-file credentials/private_key.crt
python manage.py runserver_plus --cert-file credentials/server.crt
python manage.py runserver_plus --key-file credentials/private_key.key

# error
python manage.py runserver_plus --cert-file credentials/server.pem
python manage.py runserver_plus --cert-file credentials/server.key
python manage.py runserver_plus --cert-file credentials/server.csr
python manage.py runserver_plus --key-file credentials/private_key.pem
python manage.py runserver_plus --key-file credentials/private_key.crt
python manage.py runserver_plus --key-file credentials/server.key --cert-file credentials/server.pem
python manage.py runserver_plus --key-file credentials/private_key.key --cert-file credentials/server.crt
python manage.py runserver_plus --key-file credentials/private_key.pem --cert-file credentials/server.crt
python manage.py runserver_plus --key-file credentials/private_key.key --cert-file credentials/server.key
python manage.py runserver_plus --key-file credentials/private_key.crt --cert-file credentials/server.crt


# gunicorn speechclassification.wsgi
# Donni Richasdy Certificate
# Request to Enter PEM pass phrase for every html component if private_key has pass phrase
gunicorn --certfile=credentials/server.pem --keyfile=credentials/private_key.pem speechclassification.wsgi
gunicorn --certfile=cert.pem --keyfile=key.pem speechclassification.wsgi

# *.localhost/CN=localhost
# Dummy Certificate
gunicorn --certfile=credentials/server.crt --keyfile=credentials/server.key speechclassification.wsgi
gunicorn --certfile=credentials/private_key.crt --keyfile=credentials/private_key.key speechclassification.wsgi

# error
gunicorn --certfile=credentials/server.pem --keyfile=credentials/private_key.pem speechclassification.wsgi

gunicorn --certfile=credentials/server.pem --keyfile=credentials/server.key speechclassification.wsgi
gunicorn --certfile=credentials/server.crt --keyfile=credentials/server.key speechclassification.wsgi
gunicorn --certfile=credentials/server.pem --keyfile=credentials/private_key.pem speechclassification.wsgi
gunicorn --certfile=credentials/server.crt --keyfile=credentials/private_key.key speechclassification.wsgi
gunicorn --certfile=credentials/server.crt speechclassification.wsgi
gunicorn --certfile=credentials/private_key.crt speechclassification.wsgi
gunicorn --keyfile=credentials/private_key.key speechclassification.wsgi
gunicorn --keyfile=credentials/server.key speechclassification.wsgi

