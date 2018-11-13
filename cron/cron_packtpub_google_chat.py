from crontab import CronTab

cron = CronTab(user='xerpa')  
job = cron.new(command='../script/packtpub.py')  
job.hour.every(11)

cron.write()    