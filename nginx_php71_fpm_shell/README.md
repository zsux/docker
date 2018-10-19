
- https://hub.docker.com/r/dockerphp/nginx/
- https://github.com/OsLab/docker-php-nginx


# install 

- python2.7
- php7
- nginx

### Build
    
    docker build -t pt_nginx_php_fpm_prod_1:latest .
    
    docker run -it pt_nginx_php_fpm_prod_1:latest bash

    docker run -it pt_nginx_php_fpm_prod_1:latest \
        bash -c "boot.py --pre_init="ls /opt" --init=1 --after_init="ls /" --boot=nginx,php-fpm,sshd,shell,crond --start=1"

# push

    docker login --username=dholer@163.com registry.cn-shanghai.aliyuncs.com
    sudo docker tag 57a42b1b52aa registry.cn-shanghai.aliyuncs.com/loan-market/repo:nginx-php71-fpm-2.3
    sudo docker push registry.cn-shanghai.aliyuncs.com/loan-market/repo:nginx-php71-fpm-2.3

   
#release

* registry.cn-shanghai.aliyuncs.com/loan-output/repo:nginx-php71-fpm-2.3

> 1. change php error_reporting

* registry.cn-shanghai.aliyuncs.com/loan-output/repo:nginx-php71-fpm-2.0

> 1. change php-fpm

* registry.cn-shanghai.aliyuncs.com/loan-output/repo:nginx-php71-fpm-1.8

> 1. change nginx php-fpm config

* registry.cn-shanghai.aliyuncs.com/loan-output/repo:nginx-php71-fpm-1.7

> 1. change php fpm config

* registry.cn-shanghai.aliyuncs.com/loan-output/repo:nginx-php71-fpm-1.6

> 1. change php config

* registry.cn-shanghai.aliyuncs.com/loan-output/repo:nginx-php71-fpm-1.5

> 1. change supervisor log

* registry.cn-shanghai.aliyuncs.com/loan-output/repo:nginx-php71-fpm-1.4

> 1. change boot.py

* registry.cn-shanghai.aliyuncs.com/loan-output/repo:nginx-php71-fpm-1.2

> 1. pre init and after init
    
    
* registry.cn-shanghai.aliyuncs.com/loan-output/repo:nginx-php71-fpm-1.1

> 1. init
