FROM ubuntu:16.04
MAINTAINER Joseph zhou "joseph.zhou@gmail.com"
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y
RUN apt-get install -y build-essential tzdata locales
RUN date
RUN echo "Asia/Shanghai" > /etc/timezone \
    && dpkg-reconfigure tzdata

RUN apt-get install -y \
      php \
      php-cli \
      php-gd \
      php-json \
      php-ldap \
      php-mbstring \
      php-mysql \
      php-curl \
      php-bcmath \
      php-mcrypt \
      php-opcache \
      php-pgsql \
      php-sqlite3 \
      php-xml \
      php-xsl \
      php-zip \
      php-soap \
      php-redis \
      php-mongodb \
      php-xdebug \
      composer

RUN apt-get install -y git curl unzip wget vim telnet rsync

RUN apt-get install -y python-pip \
    && pip install -U pip
RUN mkdir /opt/composer

RUN cd /opt/composer \
    && composer config -g repo.packagist composer https://packagist.phpcomposer.com \
    && composer require overtrue/phplint --prefer-source --no-interaction \
    && ln -s /opt/composer/vendor/bin/phplint /bin/phplint

RUN cd /opt/composer && composer require phpunit/phpunit ^6.4 --prefer-source --no-interaction \
    && composer require "phpunit/php-invoker" --prefer-source --no-interaction \
    && ln -s /opt/composer/vendor/bin/phpunit /bin/phpunit \
    && sed -i 's/nn and/nn, Julien Breux (Docker) and/g' /opt/composer/vendor/phpunit/phpunit/src/Runner/Version.php

RUN apt-get install -y redis-tools mysql-client
RUN apt-get install -y redis-server
RUN apt-get install -y mysql-server

