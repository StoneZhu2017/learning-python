#!/usr/bin/python
#filename:backup_ver2.py
import os
import time

#1.The files and directories to be backed up are specified in a list
source=[r'E:\python361\scripts',r'E:\python361\tools']
#2.The backup must be stored in a main backup directory
target_dir='E:\\test\\'
#3.The files are backed up into a zip file
#4.The current day is the name of the subdirectory in the main directory
today=target_dir+time.strftime("%Y%m%d")
now=time.strftime("%H%M%S")
#create the subdirectory if it isn't already
if not os.path.exists(today):
    os.mkdir(today)     #make directory
    print('Successfully created directory',today)

#The name of the zip file
target=today+os.sep+now+'.zip'

zip_command="7z a %s %s"%(target,' '.join(source))

#run the backup
if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup Failed!')
