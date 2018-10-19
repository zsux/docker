FROM dockerphp/nginx:7.1-stretch
MAINTAINER Barry <dhole.me@gmail.com>

USER root
# Copy all scripts
COPY image/scripts /tmp/
COPY image/config /
COPY image/scripts/bin /opt/scripts

RUN chmod +x /tmp/*.sh && \
    sh /tmp/env.sh

RUN apt-get -y update \
    && apt-get install -y openssh-server --no-install-recommends

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*

# Copy config

ADD ./.docker.boot.py /bin/boot.py

RUN chmod +x /bin/boot.py /etc/motd

WORKDIR /code
USER www

RUN mkdir /home/www/.ssh/ && touch /home/www/.ssh/authorized_keys && chmod 600 /home/www/.ssh/authorized_keys \
    && chmod 700 /home/www/.ssh

EXPOSE 22 80 443 2022 8081

