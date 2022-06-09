#Deriving the latest base image
FROM python:latest

WORKDIR /usr/app/src

ADD rsa.py ./
ADD generate_primes.py ./
EXPOSE 8080


CMD [ "python3", "./rsa.py"]