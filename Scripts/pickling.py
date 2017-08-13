#!/usr/bin/python3
#filename:pickling.py

#import cPickle as p
import pickle as p

shoplistfile=r'e:\test\shoplist.data'
#the name of the file where we will store the object

shoplist=['apple','-mango','-carrot']

#Write to the file
fp=open(shoplistfile,'w')
#p.dump(shoplist,fp)  #dump the object to a file
p.dump(shoplist,fp)
fp.close()

del shoplist    #remove the shoplist

#Read back from the storage
fr=open(shoplistfile)
storedlist=p.load(fr)
print(storedlist)
