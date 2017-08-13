#!/usr/bin/python3
#filename:class_init.py

class Person:
    def __init__(self,name):
        self.name=name

    def sayHi(self):
        print('Hi %s, how are you?'%self.name)

p=Person('Stone')
p.sayHi()
