FROM python:3.8-slim-buster

ARG SETTINGS

ENV MICROSERVICE=/home/app/microservice/
ENV SETTINGS=${SETTINGS}

RUN mkdir -p $MICROSERVICE
#RUN mkdir -p $MICROSERVICE/static


WORKDIR $MICROSERVICE

RUN apt-get update \
    && apt-get -y install libpq-dev gcc logrotate \
    && pip install psycopg2
    
COPY ./requirements.txt .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput --clear

CMD ["gunicorn", "--timeout", "0", "--bind", ":8000", "--workers", "3", "ai.wsgi:application"]