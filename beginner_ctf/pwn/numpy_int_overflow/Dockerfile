#Deriving the latest base image
FROM python:latest

WORKDIR /usr/app/src
RUN pip install numpy

ADD code_for_docker.py ./
EXPOSE 8080


CMD [ "python3", "./code_for_docker.py"]