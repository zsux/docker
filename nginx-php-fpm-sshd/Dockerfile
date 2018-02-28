FROM richarvey/nginx-php-fpm:latest
MAINTAINER Barry "dhole.me@gmail.com"

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

RUN apk --update add --no-cache openssh bash \
  && sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \
  && sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin without-password/' /etc/ssh/sshd_config \
  && sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config \
  && sed -ri 's/^#PasswordAuthentication\s+.*/PasswordAuthentication no/' /etc/ssh/sshd_config \
  && echo "root:root" | chpasswd \
  && rm -rf /var/cache/apk/*

RUN sed -ie 's/#Port 22/Port 22/g' /etc/ssh/sshd_config
RUN sed -ri 's/#HostKey \/etc\/ssh\/ssh_host_key/HostKey \/etc\/ssh\/ssh_host_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_rsa_key/HostKey \/etc\/ssh\/ssh_host_rsa_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_dsa_key/HostKey \/etc\/ssh\/ssh_host_dsa_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_ecdsa_key/HostKey \/etc\/ssh\/ssh_host_ecdsa_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_ed25519_key/HostKey \/etc\/ssh\/ssh_host_ed25519_key/g' /etc/ssh/sshd_config
RUN /usr/bin/ssh-keygen -A
RUN ssh-keygen -t rsa -b 4096 -f  /etc/ssh/ssh_host_key
RUN mkdir -p /etc/supervisor/conf.d

ADD conf/supervisord.conf /etc/supervisord.conf
ADD conf/supervisor_sshd.conf /root/supervisor_sshd.conf
ADD conf/supervisor_nginx.conf /root/supervisor_nginx.conf
ADD conf/supervisor_fpm.conf /root/supervisor_fpm.conf
ADD conf/supervisor_crond.conf /root/supervisor_crond.conf

RUN echo 'cp /root/supervisor_sshd.conf /etc/supervisor/conf.d' > /bin/en_sshd
RUN echo 'cp /root/supervisor_nginx.conf /etc/supervisor/conf.d' > /bin/en_nginx
RUN echo 'cp /root/supervisor_fpm.conf /etc/supervisor/conf.d' > /bin/en_fpm
RUN echo 'cp /root/supervisor_crond.conf /etc/supervisor/conf.d' > /bin/en_crond

RUN chmod +x /bin/en_sshd
RUN chmod +x /bin/en_nginx
RUN chmod +x /bin/en_fpm
RUN chmod +x /bin/en_crond

ADD conf/check_crontab.sh /var/run/check_crontab.sh
RUN chmod +x /var/run/check_crontab.sh

RUN mkdir -p /opt/etc/cron/
ADD conf/crontab.cron /opt/etc/cron/crontab.cron
RUN crontab /opt/etc/cron/crontab.cron
RUN rm -rf /var/cache/apk/*
EXPOSE 22
