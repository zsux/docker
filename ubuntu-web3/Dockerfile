FROM registry.cn-shanghai.aliyuncs.com/pt/ubuntu-nginx-php-fpm
MAINTAINER Joseph zhou "joseph.zhou@gmail.com"

# update source
#RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
#RUN sed -i 's/archive.ubuntu.com/mirrors.aliyuncs.com/g' /etc/apt/sources.list

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get clean
RUN apt-get update  --fix-missing

RUN mkdir -p /var/supervisor/

RUN echo "[program:sshd]"    >> /var/supervisor/sshd.conf \
    && echo "command=/usr/sbin/sshd -D"  >> /var/supervisor/sshd.conf

RUN echo "[program:cron]"    >> /var/supervisor/cron.conf \
    && echo 'command=/bin/bash -c "cron -f"'  >> /var/supervisor/cron.conf

RUN echo "[program:nginx]"    >> /var/supervisor/nginx.conf \
    && echo 'command=/usr/sbin/nginx -g "daemon off;"'  >> /var/supervisor/nginx.conf

RUN echo "[program:php-fpm]"    >> /var/supervisor/php-fpm.conf \
    && echo 'command=/usr/sbin/php-fpm7.0 -F'  >> /var/supervisor/php-fpm.conf

#clean
#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /root
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
