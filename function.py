# -*- coding: utf-8 -*-

a=abs(-20.5)
print(a)

b=max(1,2,5,3,8)
print(b)

c=int(12.4)
print(c)

d=str(4.45)
print(d)

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-99))

def nop():
    pass


import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

r=move(100,100,60,math.pi/6)
print(r)

def quadratic(a,b,c):
    if not isinstance(a,(int,float))\
    or not isinstance(b,(int,float))\
    or not isinstance(c,(int,float)):
        raise TypeError('bad operand type')
        
    tmp=b*b-4*a*c
    if tmp>0:
        s1=(-b+math.sqrt(tmp))/(2*a)
        s2=(-b-math.sqrt(tmp))/(2*a)
        return s1,s2
    elif tmp==0:
        s1=(-b+math.sqrt(tmp))/(2*a)
        return s1
    else:
        return None
    
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))   
    
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
    
print(power(5,3))


def calc(numbers):
    sum=0
    for n in numbers:
        sum= sum +n*n
    return sum

print(calc([1,2,3,4,5]))
#print(calc(1,2,3))

def calc1(*numbers):
    sum=0
    for n in numbers:
        sum= sum +n*n
    return sum

print(calc1(1,2,3))

def product(*num):
    if num==():
        raise TypeError('miss argument')
    p=1
    for x in num:
        p=p*x
    return p

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))

