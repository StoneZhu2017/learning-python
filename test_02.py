#!/usr/bin/python3

#coding=utf-8

#filename:test_02.py
# author by:www.runoob.com

#用户输入摄氏温度
#接收用户收入
celsius=float(input('输入摄氏温度：'))

#计算华氏温度
fahrenheit=(celsius*1.8)+32
print('%0.1f摄氏温度转化为华氏温度为%0.1f'%(celsius,fahrenheit))

'''
import random
print(random.randint(0,10))


a=float(input('请输入三角形的第一条边长：'))
b=float(input('请输入三角形的第二条边长：'))
c=float(input('请输入三角形的第二条边长：'))

#计算半周长
s=(a+b+c)/2

#计算面积
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('三角形面积为:%0.2f'%area)
'''
