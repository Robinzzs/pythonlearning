# -*- coding: utf-8 -*-

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(1))

print(fact(5))

print(fact(100))

#递归调用次数过多会导致栈溢出

#尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product)

#print(fact(1000))


