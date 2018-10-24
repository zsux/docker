
- https://hub.docker.com/r/dockerphp/nginx/
    - https://github.com/OsLab/docker-php-nginx


# install 

- python3
- php7
- nginx

### Build
    
    docker build -t pt_nginx_php_fpm_prod_1:latest . && docker images | grep pt_nginx_php_fpm_prod_1
    docker build -t pt_nginx_php_fpm_prod_2:latest . && docker images | grep pt_nginx_php_fpm_prod_2
    
    docker build -t pt_nginx_php_fpm_prod_1:latest . && \
     docker run -it -e "PK_root_1=root_1" -e "PK_test_1=www_1" -e "PK_www=www_0" \
          pt_nginx_php_fpm_prod_1:latest bash -c "boot.py --init_user=1 --boot=sshd --start=1"
    
    docker run pt_nginx_php_fpm_prod_1:latest \
        bash -c "sudo boot.py --wwwroot=/code/web --pre_init='ls /opt' --boot=nginx,php-fpm,sshd,crond --start=1"

    
    docker run -it registry.cn-shanghai.aliyuncs.com/pt/repo:np71-1.9 \
        bash -c "boot.py --init='ls -al' --boot='nginx,php-fpm,shell,sshd'"
                
