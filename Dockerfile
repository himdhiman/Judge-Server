FROM python:3.6-alpine
COPY requirements.txt /app/requirements.txt

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN set -ex \
    && python -m pip install --upgrade pip \
    && pip install -r /app/requirements.txt

WORKDIR /app

ADD . .

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "JudgeServer.wsgi:application"]

# CMD gunicorn JudgeServer.wsgi:application --bind 0.0.0.0:$PORT