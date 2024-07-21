FROM ubuntu:latest
LABEL authors="nazar"
FROM python:3.9-slim
WORKDIR /myApp
COPY requirements.txt /myApp/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /myApp
EXPOSE 80


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]