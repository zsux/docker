#!/usr/bin/env python
import argparse
import os
import sys
import logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

parser = argparse.ArgumentParser(description='DOCKER BOOT')
parser.add_argument('--start', help='start', default="0")
parser.add_argument('--boot', help='boot', default="")
parser.add_argument('--auth', help='basic auth', default="")
parser.add_argument('--pre_init', help='pre init', default="")
parser.add_argument('--after_init', help='after init', default="")
parser.add_argument('--vh', help='vhost', default="")
parser.add_argument('--au', help='auth', default="")
parser.add_argument('--init', help='init', default="")
parser.add_argument('--init_user', help='init_user', default="")
parser.add_argument('--web', help='www root dir', default="")
parser.add_argument('--run', help='run', default="")

args = parser.parse_args()
start = args.start
boot = args.boot
auth = args.auth
pre_init = args.pre_init
after_init = args.after_init
init = args.init
init_user = args.init_user
vh = args.vh
au = args.au
web = args.web
run = args.run

logging.info("booting...,%s",args)

def os_system(cmd):
    logging.info( "> exec: %s",cmd)
    os.system(cmd)

os_system("id")
os_system("pwd")

def do_init_user():
    id = 1201
    for env_key in os.environ:
        if env_key.startswith("PK_"):
            key = env_key.replace("PK_", "")
            t = key.split("_")
            username = t[0]
            public_key = os.getenv(env_key,None)
            print( ">> do_init_user: {0}@{1}".format(username,public_key))
            if public_key is None:
                continue
            if username == "root":
                print("ignore root")
            elif username == "www":
                os_system("sudo echo {0} >> /home/www/.ssh/authorized_keys".format(public_key))
            else:
                id += 1
                os_system("sudo useradd --uid {0} --gid www --shell /bin/bash --create-home {1}".format(id,username))
                os_system("echo '{0}:{0}_2018' | sudo chpasswd".format(username))
                os_system("sudo su - {} -c 'id'".format(username))
                os_system("sudo su - {} -c 'mkdir -p ~/.ssh'".format(username))
                os_system("sudo su - {0} -c 'echo {1} >> ~/.ssh/authorized_keys'".format(username,public_key))
                os_system("sudo su - {0} -c 'chmod 600 ~/.ssh/authorized_keys'".format(username))

if len(web) > 0:
    cmd = "sudo sed -i 's/root \/code/root {}/g' /etc/nginx/sites-enabled/default.conf".format(web.replace("/",'\/'));
    os_system(cmd)

if len(run) > 0 and os.getenv(run,None) is not None:
    os_system("echo ${0} | base64 --decode > {1} && cat {1} && echo && sh {1}".format(run,'/tmp/run.sh'))

if len(pre_init) > 0:
    os_system(pre_init)

if len(init) > 0:
    os_system(init)

if len(after_init) > 0:
    os_system(after_init)

if len(init_user) > 0:
    do_init_user()

for item in boot.split(","):
    if len(item) == 0:
        continue
    os_system("sudo cp /etc/supervisor/conf_d/{0}.conf /etc/supervisor/conf.d/{0}.conf".format(item))

if len(vh) > 0 and os.getenv(vh,None) is not None:
    os_system("sudo chmod 777 /etc/nginx/nginx.conf && echo $NGINX_VHOSTS | base64 --decode > /etc/nginx/nginx.conf".format(vh))

if len(au) > 0 and os.getenv(au,None) is not None:
    os_system("sudo touch /etc/nginx/.htpasswd && sudo chmod 777 /etc/nginx/.htpasswd && echo ${} > /etc/nginx/.htpasswd".format(au))

if start == '1':
    print("starting")
    os_system("sudo /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf")
