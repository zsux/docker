#!/usr/bin/env python
#py2
import argparse
import os

parser = argparse.ArgumentParser(description='DOCKER BOOT')
parser.add_argument('--start', help='start', default="0")
parser.add_argument('--boot', help='boot', default="")
parser.add_argument('--auth', help='basic auth', default="")
parser.add_argument('--pre_init', help='pre init', default="")
parser.add_argument('--after_init', help='after init', default="")
parser.add_argument('--init', help='init', default="")
parser.add_argument('--wwwroot', help='www root dir', default="")

args = parser.parse_args()
start = args.start
boot = args.boot
auth = args.auth
pre_init = args.pre_init
after_init = args.after_init
init = args.init
wwwroot = args.wwwroot

print("booting...".format(args))

def os_system(cmd):
    print( "> exec: ".format(cmd))
    os.system(cmd)

def init_user():
    for env_key in os.environ:
        if env_key.startswith("PUB_KEY"):
            key = env_key.replace("PUB_KEY_", "")
            t = key.split("_")
            username = t[0]
            if username == "root":
                os_system("sudo mkdir -p /root/.ssh")
                os_system("sudo echo {0} >> /root/.ssh/authorized_keys".format(os.environ[env_key]))
                os_system("sudo chmod 600 /root/.ssh/authorized_keys")
            else:
                os_system("sudo useradd -G sudo -m -s '/bin/bash' {}".format(username))
                os_system("sudo echo '{0}:{0}kd123456' | chpasswd".format(username))
                os_system("sudo mkdir -p /home/{0}/.ssh".format(username))
                os_system("sudo echo {0} >> /home/{1}/.ssh/authorized_keys".format(os.environ[env_key], username))
                os_system("sudo chmod 600 /home/{0}/.ssh/authorized_keys".format(username))
                os_system("sudo chown -R {0}:{0} /home/{0}/.ssh".format(username))

if len(wwwroot) > 0:
    cmd = "sudo sed -i 's/root \/code/root {}/g' /etc/nginx/sites-enabled/default.conf".format(wwwroot.replace("/",'\/'));
    os_system(cmd)

if len(pre_init) > 0:
    os_system(pre_init)

if len(init) > 0:
    os_system(init)

if len(after_init) > 0:
    os_system(after_init)

for item in boot.split(","):
    if len(item) == 0:
        continue
    if item == "init-user":
        init_user()
    else:
        os_system("sudo cp /etc/supervisor/conf_d/{0}.conf /etc/supervisor/conf.d/{0}.conf".format(item))

if start == '1':
    print("starting")
    os_system("sudo /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf")