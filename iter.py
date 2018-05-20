# -*- coding: utf-8 -*-

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
    
    
    
#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable

a=isinstance('abc', Iterable)
print(a)

#Python内置的enumerate函数可以把一个list变成索引-元素对，
#这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['a','b','c']):
    print(i,value)
    
