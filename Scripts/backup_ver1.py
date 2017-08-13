#!/usr/bin/python
#filename:backup_ver1.py

import os
import time

#1. The files and directories to be backed up are specified in a list
source=['E:\\python361\\Scripts','E:\\python361\\tools']

#2.The backup must be stored in a main directory
target_dir='E:\\test\\'   #Remember to change this to what you will be using

#3.The files are backed up into a zip file.
#4. The name of the zip archive is the current date and time
target = target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
print(target)
#5. We use the zip command (in Unix/Linux) to put the file in a zip archive
zip_command="7z a %s %s" %(target,' '.join(source))
print(zip_command)
#6.Run the backup
if os.system(zip_command)==0:
    print('successful backup to',target)
else:
    print('Backup Failed!')

