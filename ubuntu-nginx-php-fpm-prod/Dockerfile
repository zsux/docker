FROM ubuntu:14.04
MAINTAINER Dhole "dhole.me@gmail.com"
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl
# update source
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get clean
RUN apt-get update  --fix-missing
RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q && apt-get -y -q autoclean && apt-get -y -q autoremove)
RUN apt-get install -y build-essential
RUN apt-get install -y supervisor unzip wget curl vim telnet rsync

RUN echo "Asia/Shanghai" > /etc/timezone \
    && dpkg-reconfigure tzdata
#install sshd
RUN apt-get install -y openssh-server openssh-client
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin without-password/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/^#\s+.*/PasswordAuthentication no/' /etc/ssh/sshd_config
RUN mkdir -p /var/run/sshd
#install supervisor
RUN echo "[supervisord]"    >> /etc/supervisor/supervisord.conf
RUN echo "nodaemon=true\n"  >> /etc/supervisor/supervisord.conf
RUN mkdir -p /var/log/supervisor

#install php
RUN apt-get install -y -q language-pack-en-base python-software-properties software-properties-common \
            tree openssl libpcre3 libpcre3-dev \
    && ln -s /usr/lib/x86_64-linux-gnu/libssl.so  /usr/lib \
    && LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php -y \
    && apt-get update -qq --fix-missing

RUN apt-get -q -y install php7.0-dev \
        php7.0-fpm php7.0-gd php7.0-xml php7.0-zip php7.0-mysql php7.0-mcrypt php7.0-curl php7.0-curl \
        php7.0-mbstring php7.0-bcmath \
    &&  mkdir -p /run/php \
    && sed -i "s/;date.timezone =.*/date.timezone = Asia\/Shanghai/" /etc/php/7.0/cli/php.ini \
    && sed -i "s/;date.timezone =.*/date.timezone = Asia\/Shanghai/" /etc/php/7.0/fpm/php.ini \
    && sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.0/fpm/php.ini \
    && sed -i "s/;daemonize =.*/daemonize = no/" /etc/php/7.0/fpm/php-fpm.conf \
    && sed -i "s/^listen .*/listen = 0.0.0.0:9009/" /etc/php/7.0/fpm/pool.d/www.conf \
    && sed -i 's/^listen.allowed_clients/;listen.allowed_clients/' /etc/php/7.0/fpm/pool.d/www.conf \
    && pecl install mongodb \
    && echo "extension=mongodb.so" > /etc/php/7.0/mods-available/mongodb.ini \
    && phpenmod mongodb \
    && pecl install redis \
    && echo "extension=redis.so" > /etc/php/7.0/mods-available/redis.ini \
    && phpenmod redis \
    && pecl install xdebug
    
#install nginx
RUN apt-get install -y nginx
RUN cd /tmp \
    && wget -N https://github.com/edenhill/librdkafka/archive/master.zip -O librdkafka.zip \
    && unzip librdkafka.zip \
    && rm -f librdkafka.zip \
    && cd librdkafka-master \
    && ./configure \
    && make \
    && make install \
    && pecl install rdkafka \
    && echo "extension=rdkafka.so" > /etc/php/7.0/mods-available/rdkafka.ini \
    && phpenmod rdkafka \
    && rm -rf librdkafka-master
    
RUN useradd -G sudo -m -s "/bin/bash" dev
RUN echo 'dev:888888' | chpasswd

RUN useradd -m -s "/bin/bash" test
RUN echo 'test:888888' |chpasswd

RUN useradd -m -s "/bin/bash" prod
RUN echo 'prod:888888' |chpasswd

RUN mkdir -p /home/dev/.ssh
RUN touche /home/dev/.ssh/authorized_keys
RUN chown -R dev:dev /home/dev/.ssh
RUN chmod 700 /home/dev/.ssh/
RUN chmod 600 /home/dev/.ssh/authorized_keys

RUN mkdir -p /home/test/.ssh
RUN touche /home/test/.ssh/authorized_keys
RUN chown -R test:test /home/test/.ssh
RUN chmod 700 /home/test/.ssh/
RUN chmod 600 /home/test/.ssh/authorized_keys

RUN mkdir -p /home/prod/.ssh
RUN touche /home/prod/.ssh/authorized_keys
RUN chown -R prod:prod /home/test/.ssh
RUN chmod 700 /home/prod/.ssh/
RUN chmod 600 /home/prod/.ssh/authorized_keys

#clean
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
WORKDIR /root
EXPOSE 22 80
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
