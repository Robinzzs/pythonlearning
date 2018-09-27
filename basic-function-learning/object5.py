# -*- coding: utf-8 -*-

#class Student(object):
#    def __init__(self):
#        self.name = 'Jack'
#        
#    def __getattr__(self, attr):
#        if attr=='score':
#            return 99
#        if attr=='age':
#            return lambda: 25
#    
#        raise AttributeError(' \'Student\' object has no attribute %s' % attr)
#    
#s = Student()
#print(s.name)
#
#print(s.score)
#
#print(s.age())
#
##print(s.bb)
#
#class Chain(object):
#    
#    def __init__(self, path=''):
#        self._path = path
#        
#    def __getattr__(self, path):
#        return Chain('%s/%s' % (self._path, path))
#    
#    def __str__(self):
#        return self._path
#    
#    __repr__ = __str__
#
#Chain().status.user.timeline.list #每一个 . 都是调用一次__getattr__方法


class Student(object):
    def __init__(self, name):
        self.name = name
        
    def __call__(self):
        print('My name is %s' % self.name)
        
s = Student('jack')
s()


#廖雪峰教程[面向对象高级编程]_定制类[2]
#实现一个定制类，便于链式调用
class chain(object):
    def __init__(self,path=''):
        self.path=path

    def __str__(self):#调用print()打印path
        return self.path

    def __call__(self, path):#当对实例进行调用a("xxx")时将path连接并返回一个新的实例
        return chain('%s/%s' % (self.path,path))

    def __getattr__(self, item):#当写下a.xxx时会将xxx添加到path中，并返回一个新的类
        return chain('%s/%s' % (self.path,item))
    __repr__ = __str__
    
    
a=chain()
print(a.users('michael').repos('ganma'))