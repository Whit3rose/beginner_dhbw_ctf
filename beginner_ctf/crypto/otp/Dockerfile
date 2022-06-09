#Deriving the latest base image
FROM python:latest

WORKDIR /usr/app/src

ADD server.py ./
EXPOSE 8080


CMD [ "python3", "./server.py"]
