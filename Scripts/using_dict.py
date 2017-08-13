#!/usr/bin/python
#filename: using_dict.py

#'ab' is short for 'a'ddress 'b'ook

ab={'Swaroop':'swaroopch@byteofpython.info','Larry':'larry@wall.org',\
    'Matsumoto':'matz@rub-lang.org','Spammer':'spammer@hotmail.com'}
print("Swaroop's address is %s"%ab['Swaroop'])

#Adding a key/value pair
ab['Guido']='guido@python.org'

#deleting a key/value pair
del ab['Spammer']

print('\nThere are %d contacts in the address-book\n'%len(ab))
for name,address in ab.items():
    print('contact %s at %s'%(name,address))
if 'Guido' in ab:
    print("\nGuido's address is %s"%ab['Guido'])
