FROM php:7.3-apache

ADD index.html /var/www/html/
ADD login.html /var/www/html/
ADD login.php /var/www/html/
RUN mkdir /var/www/html/assets
RUN mkdir /var/www/html/css
RUN mkdir /var/www/html/js
COPY assets/ /var/www/html/assets
COPY css/ /var/www/html/css
COPY js/ /var/www/html/js
