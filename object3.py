# -*- coding: utf-8 -*-


class Student(object):
    
    @property
    def score(self):
        return self.score
    
    
    
    @score.setter
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('must be an integer')
        if value < 0 or value > 0:
            raise ValueError('must bwtween 0~100 ')
        self.score = value
        
        
        
        
class Screen(object):
    
    @property
    def width(self):
        return self.width
    
    @width.setter
    def width(self, value):
        self.width = value
    
    @property
    def hight(self):
        return self.hight
    
    @hight.setter
    def hight(self, value):
        self.hight = value
        
    @property
    def resolution(self):
        self.resolution = self.hight * self.width
        return self.resolution
    
    
class Work(object):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    
    __repr__ = __str__

#print(Work('bbb')

#class Fib(object):
#    def __init__(self):
#        self.a, self.b = 0, 1
#        
#    def __iter__(self):
#        return self
#    
#    def __next__(self):
#        self.a, self.b = self.b, self.a + self.b
#        if self.a > 100000:
#            raise StopIteration()
#        return self.a
    
    
#class Fib(object):
#    def __init__(self):
#        self.a, self.b = 0, 1 # 初始化两个计数器a，b
#
#    def __iter__(self):
#        return self # 实例本身就是迭代对象，故返回自己
#
#    def next(self):      #python2 使用next()  python3使用__next__()
#        self.a, self.b = self.b, self.a + self.b # 计算下一个值
#        if self.a > 100000: # 退出循环的条件
#            raise StopIteration()
#        return self.a # 返回下一个值
#    
#    def __getitem__(self, n):
#        
#        
#        a, b = 1, 1
#        for x in range(n):
#            a, b = b, a+b
#        return a
#    
#for n in Fib():
#    print(n)
        

    
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop  = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L
            

    
    
        











        
        
    