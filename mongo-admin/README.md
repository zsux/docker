
### Build
    
    docker build -t pt_mongo_admin_1:latest .
    
# push

    docker login --username=dholer@163.com registry.cn-shanghai.aliyuncs.com
    docker tag 220d8c1dd96b registry.cn-shanghai.aliyuncs.com/loan-market/repo:v8js-php71-1.2
    docker push registry.cn-shanghai.aliyuncs.com/loan-market/repo:v8js-php71-1.2

   
#release

* registry.cn-shanghai.aliyuncs.com/loan-market/repo:v8js-php71-1.2

> 1. clean conf files

