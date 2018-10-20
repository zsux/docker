FROM registry.cn-shanghai.aliyuncs.com/pt/repo:np71-node-1.1

MAINTAINER Barry <dhole.me@gmail.com>
USER root

RUN rm -f /usr/bin/python \
    && ln -s /usr/bin/python2 /usr/bin/python

RUN apt-get -y update \
    && apt-get install -y python-pip \
    && pip install butterfly

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*

RUN rm -f /usr/bin/python \
    && ln -s /usr/bin/python3 /usr/bin/python

USER www
