FROM registry.cn-shanghai.aliyuncs.com/dhole/repo:nginx-php71-fpm-0.1
MAINTAINER Barry <dhole.me@gmail.com>
USER root

RUN apt-get update \
    && curl -sL https://deb.nosdesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \s
    && apt-get install -y yarn \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*

USER www
