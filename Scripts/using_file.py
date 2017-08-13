#!/usr/bin/python
#filename: using_file.py

poem='''\
programing is fun
when the work is done
if you wanna make your work also fun:
    use Python!
    中国
'''
fp=open(r'e:\test\test1.txt','w')       #open for 'w'riting
fp.write(poem)      #write text to file
fp.close()      #close the file

with open(r'e:\test\test1.txt') as fr:
    while True:
        line=fr.readline()
        if len(line)==0:
            break
        print(line)

