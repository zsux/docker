FROM boxedcode/alpine-nginx-php-fpm:latest
MAINTAINER barry <dhole.me@gmail.com>

RUN docker-php-ext-configure bcmath \
    && docker-php-ext-configure pcntl \
    && docker-php-ext-configure sockets \
    && docker-php-ext-install bcmath pcntl sockets

ENV MEMCACHED_DEPS zlib-dev libmemcached-dev cyrus-sasl-dev
RUN apk add --update libmemcached-libs zlib
RUN apk add --update --virtual .phpize-deps $PHPIZE_DEPS \
    && apk add --update --virtual .memcached-deps $MEMCACHED_DEPS \
    && pecl install memcached \
    && docker-php-ext-enable memcached

RUN pecl install mongodb \
#   && pecl install redis \
    && pecl install xdebug \
    && docker-php-ext-enable mongodb
