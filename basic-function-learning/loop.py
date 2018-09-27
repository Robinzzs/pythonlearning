# -*- coding: utf-8 -*-



sum=0
for x in [0,1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
    
print(sum)

sum=0
for x in range(10):
    sum=sum+x
    
print(sum)


sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)


n=1
while n<=100:
    if n>10:
        break
    print(n)
    n=n+1
print('END')


n=1
while n<=100:
    
    n=n+1
    if n%2==0:
        continue
    print(n)
print('END')