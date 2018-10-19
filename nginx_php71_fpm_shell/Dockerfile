FROM registry.cn-shanghai.aliyuncs.com/dhole/repo:nginx-php71-fpm-0.1
MAINTAINER Barry <dhole.me@gmail.com>
USER root

RUN apt-get -y update \
    && apt-get install -y python-pip \
    && pip install butterfly \
    && pip install tornado-http-auth

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*

USER www
