#!/usr/bin/python
#filename:reference.py

print('Simple Assignment')
shoplist=['apple','mango','carrot','banana']
mylist=shoplist #mylist is just another name pointing to the same object!
print('shoplist is',shoplist)
print('my list is',mylist)

print('\nDelete the first item:')
del shoplist[0]
print('shoplist is',shoplist)
print('my list is',mylist)

del mylist
print('\nCopy by making a full slice')
mylist=shoplist[:]
print('shoplist is',shoplist)
print('my list is',mylist)

print('mylist delete the first items')
del mylist[0]
print('shoplist is',shoplist)
print('my list is',mylist)
