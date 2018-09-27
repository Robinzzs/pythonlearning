#! /usr/bin/env python2.7

"""This script mainly about return function """


def lazy_sum(*args):
    def sum1():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum1

f = lazy_sum(1, 3, 5, 7, 9)

print(f)

print(f())
#
#def count():
#    fs=[]
#    for i in range(1,4):
#        def f():
#            return i*i
#        fs.append(f)
#    return fs
#
#f1,f2,f3=count()
##
##
#def count():
#    def f(j):
#        def g():
#            return j*j
#        return g
#    fs=[]
#    for i in range(1,4):
#        fs.append()
#    return fs


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) 
    return fs

f1,f2,f3=count()

print(f1())





def createCounter():
    i = [0]
    def counter():
        i[0] += 1
        return i[0]
    return counter

counterA = createCounter()
        
print(counterA(), counterA(), counterA(), counterA(), counterA())
        







