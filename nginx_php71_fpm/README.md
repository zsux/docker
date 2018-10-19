
- https://hub.docker.com/r/dockerphp/nginx/
- https://github.com/OsLab/docker-php-nginx


# install 

- python2.7
- php7
- nginx

### Build
    
    docker build -t pt_nginx_php_fpm_prod_1:latest .
    
    docker run -it pt_nginx_php_fpm_prod_1:latest bash
    
    docker run pt_nginx_php_fpm_prod_1:latest \
        bash -c "sudo boot.py --wwwroot=/code/web --pre_init='ls /opt' --boot=nginx,php-fpm,sshd,crond --start=1"

    docker run registry.cn-shanghai.aliyuncs.com/rcm/repo:nginx-php71-fpm-3.0 \
        bash -c "boot.py --init=1 --boot=nginx,php-fpm,sshd,crond --start=1"
        
    docker run registry.cn-shanghai.aliyuncs.com/loan-market/repo:nginx-php71-fpm-2.3 \
                bash -c "boot.py --init=1 --boot=nginx,php-fpm,sshd,crond --start=1"
                

# push

    sudo docker login --username=zhoushuxian@kdfk registry.cn-shanghai.aliyuncs.com
    sudo docker tag 747ff93f19a5 registry.cn-shanghai.aliyuncs.com/rcm/repo:nginx-php71-fpm-3.2
    sudo docker push registry.cn-shanghai.aliyuncs.com/rcm/repo:nginx-php71-fpm-3.2

   
#release

* registry.cn-shanghai.aliyuncs.com/rcm/repo:nginx-php71-fpm-3.2

> 1. change to 3.2

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
