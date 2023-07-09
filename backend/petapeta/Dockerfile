FROM python:3.9.17-bullseye

LABEL MAINTAINER="Project PetaPeta"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        libjpeg-dev \
        gcc \
        libc-dev \
        linux-headers-amd64 \
        libpq-dev \
        zlib1g \
        zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ./backend/petapeta/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN mkdir /petapeta
WORKDIR /petapeta
COPY ./backend/petapeta /petapeta

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser --disabled-password user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user

CMD sh -c "python manage.py migrate --settings app.prod_settings && python manage.py runserver 0.0.0.0:8000 --settings app.prod_settings"

