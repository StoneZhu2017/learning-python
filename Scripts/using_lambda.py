#!/usr/bin/python
#filename:lambda.py
def make_repeater(n):
    return lambda s:s*n
twice=make_repeater(2)
print(twice('word'))
print(twice(5))
