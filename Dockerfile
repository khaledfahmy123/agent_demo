FROM python:3.10

WORKDIR /app


COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

EXPOSE $PORT

CMD uvicorn main:app --host 0.0.0.0 --port $PORT
