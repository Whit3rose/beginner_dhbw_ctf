FROM ubuntu:20.04

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid
ENV APACHE_SERVER_NAME localhost

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    apache2 -y \
    ufw -y
RUN ufw allow 'Apache'
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 libapache2-mod-php7.4 php7.4-gd php-pear php7.4-apc php7.4-curl php7.4-ldap curl
RUN a2enmod php7.4
RUN service apache2 restart
RUN echo 'dhbw{check_the_path} user123456' >> /etc/passwd

EXPOSE 80

WORKDIR /var/www/html
COPY . .

CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]