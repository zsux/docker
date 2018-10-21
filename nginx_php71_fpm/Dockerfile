FROM dockerphp/nginx:7.1-stretch
MAINTAINER Barry <dhole.me@gmail.com>

USER root
COPY image/scripts /tmp/

RUN chmod +x /tmp/*.sh && \
    sh /tmp/env.sh

COPY image/config /

RUN chmod 600 /root/.ssh/authorized_keys \
    && chmod 700 /root/.ssh \
    && chmod +x /etc/update-motd.d/50-phpdocker

COPY image/scripts/bin /opt/scripts

RUN apt-get -y update \
    && apt-get install -y openssh-server --no-install-recommends \
    && echo PasswordAuthentication no >> /etc/ssh/sshd_config \
    && echo PermitRootLogin no >> /etc/ssh/sshd_config

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*

ADD ./boot.py /bin/boot.py

RUN chmod +x /bin/boot.py && chown -R www:www /home/www/

WORKDIR /code
USER www

RUN chmod 600 /home/www/.ssh/authorized_keys \
    && chmod 700 /home/www/.ssh

EXPOSE 22 80 443 2022 8081
