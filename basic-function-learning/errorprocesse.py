# -*- coding: utf-8 -*-



#俘获错误 
# try...except. （else）..finally...

import logging

#Python内置的logging模块可以非常容易地记录错误信息

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

#抛出错误

#class FooError(ValueError):
#    pass
#
#def foo(s):
#    n = int(s)
#    if n==0:
#        raise FooError('invalid value: %s' % s)
#    return 10 / n
#
#foo('0')


#def foo(s):
#    n = int(s)
#    if n==0:
#        raise ValueError('invalid value: %s' % s)
#    return 10 / n
#
#def bar():
#    try:
#        foo('0')
#    except ValueError as e:
#        print('ValueError!')
#        raise
#
### raise语句如果不带参数，就会把当前错误原样抛出
#
#bar()



from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    try:    
        r = calc('100 + 200 + 345')
    except ValueError as fir:
        print('%s in first' % fir)
    print('100 + 200 + 345 =', r)
    try:    
        r = calc('99 + 88 + 7.6')
    except ValueError as sec:
        print('%s in second' % sec)
    print('99 + 88 + 7.6 =', r)

main()









