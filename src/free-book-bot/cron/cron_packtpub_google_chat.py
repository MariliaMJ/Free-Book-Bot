import os

from crontab import CronTab


cron = CronTab(user=os.getenv('USER', 'root'))
job = cron.new(command='../script/packtpub.py')
job.hour.every(11)

cron.write()
