FROM ubuntu:14.04
MAINTAINER Joseph zhou "joseph.zhou@gmail.com"

# Keep upstart from complaining
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# update source
# RUN sudo sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list

#Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

#Timezone
RUN echo "Asia/Shanghai" > /etc/timezone
RUN dpkg-reconfigure tzdata

RUN apt-get update -qq --fix-missing && apt-get install -y -q language-pack-en-base python-software-properties software-properties-common tree openssl libpcre3 libpcre3-dev
RUN ln -s /usr/lib/x86_64-linux-gnu/libssl.so  /usr/lib
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php -y
RUN apt-get update -qq --fix-missing && apt-get -q -y install php7.0-dev php7.0-fpm php7.0-cli php7.0-gd php7.0-xml php7.0-mysql php7.0-mcrypt php7.0-curl php7.0-mbstring php7.0-bcmath php7.0-zip

RUN mkdir -p /run/php
RUN sed -i "s/;date.timezone =.*/date.timezone = Asia\/Shanghai/" /etc/php/7.0/cli/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = Asia\/Shanghai/" /etc/php/7.0/fpm/php.ini
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.0/fpm/php.ini
RUN sed -i "s/;daemonize =.*/daemonize = no/" /etc/php/7.0/fpm/php-fpm.conf
RUN sed -i "s/^listen .*/listen = 0.0.0.0:9000/" /etc/php/7.0/fpm/pool.d/www.conf
RUN sed -i 's/^listen.allowed_clients/;listen.allowed_clients/' /etc/php/7.0/fpm/pool.d/www.conf

RUN pecl install mongodb
RUN echo "extension=mongodb.so" >> /etc/php/7.0/fpm/php.ini
RUN echo "extension=mongodb.so" >> /etc/php/7.0/cli/php.ini
RUN phpenmod mongodb
RUN php -m | grep mongodb
RUN pecl install redis
RUN echo "extension=redis.so" >> /etc/php/7.0/fpm/php.ini
RUN echo "extension=redis.so" >> /etc/php/7.0/cli/php.ini
RUN phpenmod redis
RUN php -m | grep redis
RUN pecl install xdebug
RUN echo "\n[Xdebug]\nzend_extension=xdebug.so\n" >> /etc/php/7.0/fpm/php.ini
RUN echo "\n[Xdebug]\nzend_extension=xdebug.so\n" >> /etc/php/7.0/cli/php.ini
RUN phpenmod xdebug
RUN php -m | grep xdebug

RUN apt-get openssh-server
RUN mkdir -p /var/run/sshd
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin without-password/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/^#PasswordAuthentication\s+.*/PasswordAuthentication no/' /etc/ssh/sshd_config

#install supervisor
RUN apt-get install -y supervisor
RUN echo "[supervisord]"    >> /etc/supervisor/supervisord.conf
RUN echo "nodaemon=true\n"  >> /etc/supervisor/supervisord.conf

RUN echo "[program:cron]"  >> /etc/supervisor/supervisord.conf
RUN echo "command=/bin/bash -c 'cron -f'"  >> /etc/supervisor/supervisord.conf

RUN echo "[program:sshd]"  >> /etc/supervisor/supervisord.conf
RUN echo "command=/usr/sbin/sshd -D"  >> /etc/supervisor/supervisord.conf

RUN mkdir -p /var/log/supervisor

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 22
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
