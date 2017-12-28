
地址:

    docker run -it registry.cn-shanghai.aliyuncs.com/pt/ubuntu-nginx-php-fpm bash

编译

    docker build -t pt/ubuntu-nginx-php-fpm:latest .

执行
    
    docker run -it pt/ubuntu-nginx-php-fpm bash
   
   
   

"""
mkdir -p /etc/nginx/global/
host=http://47.91.226.210
curl $host/docker/opt/etc/nginx_global/yii.conf -o /etc/nginx/global/yii.conf
curl $host/docker/dev-web/nginx_test.conf -o /etc/nginx/sites-enabled/default.conf

cp /var/supervisor/nginx.conf -o /etc/supervisor/conf.d/nginx.conf
cp /var/supervisor/php-fpm.conf -o /etc/supervisor/conf.d/php-fpm.conf

"""