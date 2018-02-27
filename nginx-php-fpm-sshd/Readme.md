
编译

    docker build -t pt/nginx-php-fpm-sshd:latest .

执行
    
    docker run -it pt/nginx-php-fpm-sshd bash
    
    docker run pt/nginx-php-fpm-sshd 

    sudo docker login --username=dholer@aliyun.com registry.cn-shanghai.aliyuncs.com
    sudo docker tag a7b12b970c03 registry.cn-shanghai.aliyuncs.com/pt/nginx-php-fpm-sshd:1.0
    sudo docker push registry.cn-shanghai.aliyuncs.com/pt/nginx-php-fpm-sshd:1.0
