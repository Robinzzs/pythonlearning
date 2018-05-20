# -*- coding: utf-8 -*-

def is_odd(n):
    return n%2==1

l=list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))
print(l)



#生成器
def _odd_iter():       
    n=1
    while True:
        n=n+2
        yield n
        

#筛选函数
def _not_divisible(n):
    return lambda x:x%n>0    #????

#生成器
def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)     #3
        yield n
        it=filter(_not_divisible(n),it)
        
#1000内循环输出
for n in primes():
    if n<1000:
        print(n)
    else:
        break
    
    
#l=list(lambda a: a%7 >0)

