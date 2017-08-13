#!/usr/bin/python3.6
#filename:using_sys.py

import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe Pythonpath is',sys.path,'\n')
