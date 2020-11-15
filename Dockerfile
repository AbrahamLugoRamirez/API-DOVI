FROM python:3

LABEL Author="Nino Mercado"
LABEL version="1.0"

RUN mkdir -p /src
WORKDIR /src

# COPY requirements.txt .
COPY . .

RUN pip3 install -r requirements.txt