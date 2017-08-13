#!/usr/bin/python
#filename: backup_ver3.py
import os
import time
source=[r'E:\python361\scripts',r'E:\python361\tools']
target_dir='E:\\test\\'
today=target_dir+time.strftime('%Y%m%d')
print('today:',today)
now=time.strftime('%H%M%S')
print('now:',now)

comment=input('Enter a comment-->')
if len(comment)==0:     #check if a comment was entered
    target=today+os.sep+now+'.zip'
else:
    target=today+os.sep+now+'_'+comment.replace(' ',' ')+'.zip'

#Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)     #make directory
    print('Successfully created directory',today)

zip_command='7z a %s %s'%(target, ' '.join(source))

if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print("Backup Failed!")
    
    
