#!/usr/bin/python3
'''
#filename:test_01.py
#author by:Stone

#import datetime

import datetime
def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday

print(getYesterday())

print('Hello world!')

num1=int(input("请输入第一个数字:"))
num2=int(input('请输入第二个数字：'))

sum1=int(float(num1)+float(num2))

print('num1=%d,num2=%d'%(num1,num2))
print('num1+num2=',sum1)
'''
num=float(input('请输入一个数字：'))
num_sqrt=num**0.5
print('%0.3f的平方根是%0.3f'%(num,num_sqrt))
