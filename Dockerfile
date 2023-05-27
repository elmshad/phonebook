FROM python:3.8
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./app/requirements.txt /app/
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install gettext -y
RUN apt-get install gcc -y
RUN apt-get install libasprintf-dev -y
RUN apt-get install libgettextpo-dev -y
RUN apt-get install gettext-doc -y
RUN apt-get install autopoint -y
# RUN django-admin compilemessages -l en
# RUN django-admin compilemessages -l ar


COPY ./app/ /app/