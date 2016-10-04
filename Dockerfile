FROM python:2-slim

RUN mkdir /shadowsocks

WORKDIR /shadowsocks

CMD ["python", "/shadowsocks/server.py"]

RUN apt-get update && apt-get install -y python-pip git python-m2crypto git && pip install cymysql

COPY shadowsocks /shadowsocks
