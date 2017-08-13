#!/usr/bin/python
#filename:inherit.py

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('(Initialized SchoolMember:%s)'%self.name)

    def tell(self):
        '''Tell my details.'''
        print('Name:%s     Age:%d    '%(self.name,self.age))

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print('(Initialized Teacher:%s)'%self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:%d'%self.salary)

class Student(SchoolMember):
    '''Represents a Student.'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        print('(Initialized Student:%s)'%self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:%d'%self.marks)

t=Teacher('Teacher01',50,10000)
s=Student('Test01',25,90)

list1=[t,s]
for i in list1:
    i.tell()
