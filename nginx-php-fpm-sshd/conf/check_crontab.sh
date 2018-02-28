#!/usr/bin/env sh
cp /opt/etc/cron/crontab.cron /tmp/crontab.tmp
find /tmp/crontab.tmp -type f | xargs md5sum > /tmp/crontab_2.log
crontab -l > /tmp/crontab.tmp
find /tmp/crontab.tmp -type f | xargs md5sum > /tmp/crontab_1.log
diff /tmp/crontab_1.log /tmp/crontab_2.log > /tmp/crontab_3.log
Status=$?
if [ $Status = 0 ];then
    echo $(date)," no change !"
    exit
else
    echo $(date)," update crontab !"
    crontab /opt/etc/cron/crontab.cron
fi