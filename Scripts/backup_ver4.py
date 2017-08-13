#!/usr/bin/python3
#filename:backup_ver4.py
import os
import time

#1.
source=[r'e:\python361\scripts',r'e:\python361\tools']
target_dir='E:\\test\\'

today=target_dir+time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')

comment=input('Enter a comment-->')
if len(comment)==0:
    target=today+os.sep+now+'.zip'
else:
    target=today+os.sep+now+'_'+\
            comment.replace(' ','_')+'.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',today)

zip_command='7z a %s %s'%(target,' '.join(source))

if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup Failed!')
