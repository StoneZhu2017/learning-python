#!/usr/bin/python
#filename:using_file_a.py

test1='''
中国人民共和国
中国对印度
反法西斯战争
'''
fp=open(r'e:\test\test1.txt','a')
fp.write(test1)
fp.close()

with open(r'e:\test\test1.txt','r') as fr:
    while True:
        line=fr.readline()
        if len(line)==0:
            print('No data')
            break
        print(line)

