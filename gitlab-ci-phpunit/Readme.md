#gitlab-ci-phpunit

编译

    docker build -t pt/gitlab-ci-phpunit:latest .

执行
    
    docker run -it pt/gitlab-ci-phpunit bash
    docker run -it dhole/gitlab-ci-phpunit:0.2 bash
   
    
Todo:

    - add netstat cmd
    - add mongo-client
