# -*- coding: utf-8 -*-

L=[x*x for x in range(10)]
print(L)

g=(x*x for x in range(10))
print(g)


for n in g:
    print(n)
    
def fibs(m):
    n,a,b=0,0,1
    while n<m:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

fibs(6)

def gfibs(tt):
        n,a,b=0,0,1
        
        while n<tt:
            yield b
            a,b=b,a+b
            n=n+1
        return 'done'



def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f=gfibs(6)
print(f)

#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
#如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中

#杨辉三角

def triangles():
    l=[1]
    while True:
        yield l
        l= [1]+[x+y for x,y in zip(l[:-1],l[1:])]+[1]
        
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break