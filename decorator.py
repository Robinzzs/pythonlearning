# -*- coding: utf-8 -*-

def now():
    print("2018-05-01")

f=now

import functools

print(f)


#def log(func):
#    def wrapper(*args,**kw):
#        print('call %s():'%func.__name__)
#        return func(*args,**kw)
#    return wrapper
#
#@log
#def now():
#    print('2018-05-01')



#def log(func):
#    @functools.wraps(func)
#    def wrapper(*args,**kw):
#        pritnt('call %s():'%func.__name__)
#        return func(*args,**kw)
#    return wrapper



def log(text = ''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(args, **kw):
            print('%s %s():' % (text, func.name))
            return func(args, **kw)
        return wrapper
    return decorator


@log()
def now():
    print('2018-4-25')
now()

@log('execute')
def now():
    print('2018-4-22')
now()
    

