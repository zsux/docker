FROM ubuntu:16.04
MAINTAINER Joseph zhou "joseph.zhou@gmail.com"
ENV DEBIAN_FRONTEND noninteractive
ENV INITRD No

RUN apt-get update -y
RUN apt-get install -y build-essential tzdata locales
RUN echo "Asia/Shanghai" > /etc/timezone \
    && dpkg-reconfigure tzdata

RUN apt-get install -y redis-server
RUN apt-get install -y mysql-server
RUN apt-get install -y supervisor

RUN apt-get install -y git curl unzip wget vim telnet rsync redis-tools mysql-client

RUN apt-get install -y python-pip \
    && pip install -U pip

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

RUN mkdir /opt/composer

RUN cd /opt/composer \
    && composer config -g repo.packagist composer https://packagist.phpcomposer.com \
    && composer require overtrue/phplint --prefer-source --no-interaction \
    && ln -s /opt/composer/vendor/bin/phplint /bin/phplint

RUN cd /opt/composer && composer require phpunit/phpunit ^6.4 --prefer-source --no-interaction \
    && composer require "phpunit/php-invoker" --prefer-source --no-interaction \
    && ln -s /opt/composer/vendor/bin/phpunit /bin/phpunit \
    && sed -i 's/nn and/nn, Julien Breux (Docker) and/g' /opt/composer/vendor/phpunit/phpunit/src/Runner/Version.php

#RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf
#ADD set-mysql-password.sh /tmp/set-mysql-password.sh
#RUN /bin/sh /tmp/set-mysql-password.sh

#VOLUME ["/var/lib/mysql"]
#EXPOSE 3306

#RUN echo "[program:redis]"    >> /var/supervisor/redis.conf \
#    && echo "command=/usr/bin/redis-server"  >> /var/supervisor/redis.conf

#RUN echo "[program:mysql]"    >> /var/supervisor/mysql.conf \
#    && echo "command=/usr/bin/pidproxy /var/run/mysqld/mysqld.pid /usr/bin/mysqld_safe"  >> /var/supervisor/mysql.conf


RUN apt-get clean
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
