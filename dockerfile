FROM python:3.7.8

RUN mkdir -p /var/srv/src

COPY ./requirements.txt /var/srv/
COPY ./src/* /var/srv/src/

RUN pip install -U pip \
    & pip install -r /var/srv/requirements.txt

CMD [ "python", "/var/srv/src/app.py" ]
