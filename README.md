# Speech Classification
Interview grading with text to speech and text classification

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need to install

```
docker
docker-compose
```

### Installing

A step by step to get development env running

docker configuration :

```sh
docker-compose up
```

## Running the tests

```sh
docker-compose run \
  -e DJANGO_SETTINGS_MODULE=django_app.settings.testing \
  --no-deps --rm web py.test;
```

## Deployment

System deploy on heroku container environment

```sh
heroku login -i
heroku create speech-classification-donni

heroku container:login
heroku container:push web
heroku container:release web
heroku open

```

## Built With

* [Django](https://www.djangoproject.com/) - Web Framework
* [SQLite](https://www.sqlite.org) - Database Management
* [gunicorn](http://gunicorn.org) - Web Server

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Style Guide

Use [pep-008](https://www.python.org/dev/peps/pep-0008) for tylr guide

## Versioning

Use [SemVer](http://semver.org/) for versioning. 

## Future Works
* https://krzysztofzuraw.com/blog/2016/django-celery-rabbit-part-one.html
* https://krzysztofzuraw.com/blog/2016/django-cookiecutter.html
* https://stackabuse.com/asynchronous-tasks-in-django-with-redis-and-celery/ 

## Authors

* **Donni Richasdy** - *Initial work* - [richasdy](https://github.com/richasdy)

See also the list of [contributors](https://github.com/richasdy/speech-classification-dri/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Kemas Muslim
* Nurul Ikhsan
* Isman Kurniawan
* Jofardo Adlinnas
* Zinedine Zidane Hanjar
* Daniel Gentha Ivan Desantha