# -*- coding: utf-8 -*-

_metaclass_ = type

class Person:
    
    def setName(self,name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def greet(self):
        print("hello,world! I'm %s. " % self.name)

foo=Person()
bar=Person()

foo.setName('luke skywalker')
bar.setName('anakin skywalker')

# foo.name='bbbb'
foo.greet()
bar.greet()

