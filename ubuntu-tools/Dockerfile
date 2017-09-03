FROM ubuntu:14.04
MAINTAINER Joseph zhou "dhole.me@gmail.com"
#RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyuncs.com/g' /etc/apt/sources.list
RUN apt-get update  --fix-missing
RUN apt-get install -y git curl rsync wget unzip vim build-essential
RUN apt-get install -y redis-tools mysql-client
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
RUN echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
RUN apt-get update --fix-missing
RUN apt-get install -y mongodb-org-shell
RUN mkdir -p /var/run/sshd
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin without-password/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/^#PasswordAuthentication\s+.*/PasswordAuthentication no/' /etc/ssh/sshd_config
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
