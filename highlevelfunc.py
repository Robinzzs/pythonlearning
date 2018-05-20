# -*- coding: utf-8 -*-

print(abs(-10))

print(abs)

f=abs

print(f(-9))

def add(x,y,f):
    return f(x)+f(y)

print(add(5,-6,abs))


def f(x):
    return x*x


r=map(f,[1,2,3,4,5,6,7,8,9])

print(r)
print(list(r))

print(list(map(str,[1,2,3,4,5,6,7,8,9])))

from functools import reduce

def add(x,y):
    return x+y

num=reduce(add,[1,3,5,7,9])
print(num)

def fn(x,y):
    return x*10+y

num2=reduce(fn,[1,3,5,7,9])
print(num2)



DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))



DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))



def normalize(name):
    name=name[:1].upper()+name[1:].lower()
    return name

L1 = ['adam', 'LISA', 'barT'] 
L2 = list(map(normalize, L1)) 
print(L2)

def prod(L):
    def f(x,y):
        return x*y
    return reduce(f,L)

print('3 5  7 9 =', prod([3, 5, 7, 9]))


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    pos=s.find('.')
    ss=s[:pos]+s[pos+1:]
    def char2num(c):
        if c.isnumeric():
            return DIGITS[c]
    def fn(x,y):
        return x*10+y
    ans=reduce(fn,map(char2num,ss))
    n=len(ss)-pos
    while n:
        ans=ans/10
        n-=1
    return ans

print('str2float(\'123.456\') =', str2float('123.456'))
        
    

    
    
    
    
    
    
    