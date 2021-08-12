FROM python:3.7.3-alpine3.8
RUN apk add --nocache build-base
WORKDIR /app
COPY rpc.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD uvicorn api:qpp --host 0.0.0.0 --port 80
