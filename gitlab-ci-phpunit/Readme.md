#gitlab-ci-phpunit

编译

    docker build -t pt/gitlab-ci-phpunit:latest .

执行
    
    docker run -it pt/gitlab-ci-phpunit bash
   
Todo:

    - add netstat cmd
    - timezone
    - add mongo-client
