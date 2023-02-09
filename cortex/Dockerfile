FROM python:3.10.5-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app/

RUN apt-get update && apt-get install libpq-dev gcc -y

ADD requirements /app/
RUN pip install -r requirements

ADD . /app/

ADD entrypoint.sh /app/
ENTRYPOINT ["./entrypoint.sh"]