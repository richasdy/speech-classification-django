FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# collect static files
# RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# run gunicorn
CMD gunicorn speechclassification.wsgi:application --bind 0.0.0.0:$PORT