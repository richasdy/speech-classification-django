FROM python:3.7.3-alpine
# FROM nickgryg/alpine-pandas
COPY . /app
WORKDIR /app

RUN apk --update add --no-cache build-base
RUN apk --update add --no-cache alpine-sdk
RUN apk --update add --no-cache g++
RUN apk --update add --no-cache make
RUN apk --update add --no-cache libc-dev
RUN apk --update add --no-cache wget
RUN apk --update add --no-cache gfortran
RUN apk --update add --no-cache perl

# upgrade pip
RUN pip install --no-cache-dir -U pip

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



# install python dep
RUN pip install --no-cache-dir -r requirements.txt

# collect static files
# RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# run gunicorn
CMD gunicorn speechclassification.wsgi:application --bind 0.0.0.0:$PORT