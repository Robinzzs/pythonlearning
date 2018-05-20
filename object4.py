# -*- coding: utf-8 -*-

#class Student(object):
#    def __init__(self, name):
#        self.name = name
#    
#    
#s = Student('bob')
#s.score = 90
#
#class Student():
#    pass
#
#
#s = Student()
#s.name='jack'
#print(s.name)
#   
#def set_age(self,age):
#    self.age=age
#    
#from types import MethodType
#
#s.set_age = MethodType(set_age, s)
#
#s.set_age(25)
#
#print(s.age)
#
#def set_score(self, score):
#    self.score = score
#    
#Student.set_score = set_score
#
#s.set_score(100)
#print(s.score)

class Student(object):
    __slots__ = ('name', 'age')
    
s = Student()
s.name = 'jack'
print(s.name)
s.age = 20
print(s.age)
s.score = 99
print(s.score)




#s=Student()
#print(s.name)