# Install Docker on Ubuntu 16.04.2 LTS


    sudo apt install \
        linux-image-extra-$(uname -r) \
        linux-image-extra-virtual
        
    sudo apt install \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common
        
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    
    sudo add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
       $(lsb_release -cs) \
       stable"
       
    sudo apt update
    sudo apt install docker-ce
    sudo curl -L https://github.com/docker/compose/releases/download/$dockerComposeVersion/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    docker-compose --version

    
# Install Docker on Ubuntu 14.04
 
- https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-using-the-repository
- 
    sudo apt-get update
    sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo apt-key fingerprint 0EBFCD88
    sudo add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
       $(lsb_release -cs) \
       stable"
    sudo apt-get update
    sudo apt-get install docker-ce
    
    sudo useradd username docker

On production systems, you should install a specific version of Docker CE instead of always using the latest. This output is truncated. List the available versions.

    apt-cache madison docker-ce
    sudo apt-get install docker-ce=<VERSION>


# install docker-compose

    sudo curl -L https://github.com/docker/compose/releases/download/1.14.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    docker-compose --version

# 常用
将镜像推送到registry：

## 停止所有的container，这样才能够删除其中的images：

    docker stop $(docker ps -a -q)

## 如果想要删除所有container的话再加一个指令：

    docker rm $(docker ps -a -q)
    
## 删除所有停止的container

    sudo docker ps -a | grep Exit | cut -d ' ' -f 1 | xargs sudo docker rm

## 查看当前有些什么images

    docker images

## 删除images，通过image的id来指定删除谁

    docker rmi <image id>

## 想要删除untagged images，也就是那些id为<None>的image的话可以用

    docker rmi $(docker images | grep "^<none>" | awk "{print $3}")
    docker rmi $(docker images | grep "^pt/nginx-review " | awk "{print $3}")
    nohup sudo docker rmi $(sudo docker images | grep "^registry.cn-shanghai.aliyuncs.com/kd/test-cluster-jsqb" | awk "{print $3}") &

## 要删除全部image的话

    docker rmi $(docker images -q)

## xDebug with Docker and PHPStorm

    xdebug.remote_enable=1
    #
    docker exec -it jsqbdev_nginx-php-fpm_1 bash
    准备共钥私钥
    ssh -p 1022 -gfNL 9000:localhost:9000 root@dev.kdqugou.com
    #
    登入本地
    ssh -p 1022  -R 9000:localhost:9000 dev@dev.kdqugou.com
