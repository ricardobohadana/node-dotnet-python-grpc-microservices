FROM python:latest

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "grpcserver/server.py"]