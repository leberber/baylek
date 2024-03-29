
FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update 
RUN apt-get install -y python3.9 python3-pip 
RUN apt-get install -y git
WORKDIR /dash

COPY . .

RUN pip3 install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:443 --chdir app app:server --certfile=/fullchain.pem --keyfile=/privkey.pem
