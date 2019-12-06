# FROM python:3.7.4-alpine3.9
# FROM bitnami/python:3.7-ol-7-prod
# FROM nickgryg/alpine-pandas
# FROM ubuntu:18.04
# Docker file for a slim Ubuntu-based Python3 image

# FROM ubuntu:latest
# FROM fnndsc/ubuntu-python3

# https://www.github.com/matthewfeickert/Docker-Python3-Ubuntu
FROM matthewfeickert/docker-python3-ubuntu

MAINTAINER richasdy "donni.richasdy@gmail.com"

# RUN apt-get update \
#   && apt-get install -y python3-pip python3-dev \
#   && cd /usr/local/bin \
#   && ln -s /usr/bin/python3 python \
#   && pip3 install --upgrade pip

# ENTRYPOINT ["python3"]

COPY . /app
WORKDIR /app

# RUN apt-get install -y python3.6
# RUN apt update
# RUN apt install -y software-properties-common
# RUN add-apt-repository ppa:deadsnakes/ppa
# RUN apt install -y python3.7
# RUN apt install -y python3-pip
# RUN apk --update add --no-cache build-base
# RUN apk --update add --no-cache alpine-sdk
# RUN apk --update add --no-cache g++
# RUN apk --update add --no-cache make
# RUN apk --update add --no-cache libc-dev
# RUN apk --update add --no-cache wget
# RUN apk --update add --no-cache gfortran
# RUN apk --update add --no-cache perl
# RUN apk --update add --no-cache mkl_rt
# RUN apk --update add --no-cache openblas
# RUN apk --update add --no-cache tatlas
# RUN apk --update add --no-cache lapack_atlas
# RUN apk --update add --no-cache ptf77blas
# RUN apk --update add --no-cache ptcblas
# RUN apk --update add --no-cache f77blas
# RUN apk --update add --no-cache cblas
# RUN apk --update add --no-cache lapack

# upgrade pip
# RUN pip install --no-cache-dir -U pip

# install openblas
# RUN wget https://github.com/xianyi/OpenBLAS/archive/v0.3.6.tar.gz \
# 	&& tar -xf v0.3.6.tar.gz \
# 	&& cd OpenBLAS-0.3.6/ \
# 	&& make BINARY=64 FC=$(which gfortran) USE_THREAD=1 \
# 	&& make PREFIX=/usr/lib/openblas install

# RUN ATLAS=/usr/lib/openblas/lib/libopenblas.so LAPACK=/usr/lib/openblas/lib/libopenblas.so pip install scipy==1.3

# RUN apk add --no-cache python3-dev libstdc++ && \
#     apk add --no-cache g++ && \
#     ln -s /usr/include/locale.h /usr/include/xlocale.h

# RUN apt-get update
# RUN apt-get install -y python3.6
# RUN apt-get install -y python3-pip

# RUN sudo apt-get update
# RUN sudo apt-get install -y libpq-dev --fix-missing

# RUN sudo apt-get install -y apt-utils
RUN sudo apt-get update \
    && DEBIAN_FRONTEND=noninteractive sudo apt-get -y --no-install-recommends install libpq-dev


# RUN apk --update add --no-cache psycopg2-binary
# RUN apt-get install psycopg2-binary
# install python dep
# RUN install_packages gcc musl-dev postgresql-dev postgresql-libs .build-deps
# RUN pip install --upgrade pip
# RUN sudo pip install -H --upgrade pip 
RUN sudo pip install --no-cache-dir -r requirements.txt

# collect static files
# RUN python manage.py collectstatic --noinput

# add and run as non-root user
# RUN adduser -D myuser
# USER myuser

# run gunicorn
CMD gunicorn speechclassification.wsgi:application --bind 0.0.0.0:$PORT