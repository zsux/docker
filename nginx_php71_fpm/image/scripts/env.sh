#!/bin/bash
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"
export LANGUAGE="en_US.UTF-8"
export DEBIAN_FRONTED="noninteractive"

mkdir -p /var/run/php
rm -rf /etc/supervisor/conf.d/*
rm -rf /etc/nginx/sites-enabled/default
rm -rf /var/www/html/index.nginx-debian.html
ln -s /usr/sbin/php-fpm7.1 /usr/local/sbin/php-fpm
mkdir -p /var/log/supervisor /var/run/sshd /etc/nginx/global /usr/local/etc/php/conf.d/ /usr/local/etc/ /usr/local/etc/php-fpm.d/

#groupadd --gid 1000 php
#useradd --uid 1000 --gid php --shell /bin/bash --create-home php

groupadd --gid 1001 www
useradd --uid 1001 --gid www --shell /bin/bash --create-home www

chmod 600 /root/.ssh/authorized_keys
chmod 700 /root/.ssh

mkdir /code/
chown -R www:www /code/

echo "/etc/motd" >> /etc/bash.bashrc
#echo "alias php-xdebug='/usr/bin/php -dzend_extension=xdebug.so -dxdebug.remote_enable=1'" >> /etc/bash.bashrc
