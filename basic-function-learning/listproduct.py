# -*- coding: utf-8 -*-

l=list(range(1,10))
print(l)

L=[]
for x in range(1,11):
    L.append(x*x)

print(L)

L1=[x*x for x in range(1,11)]
print(L1)

L2=[x*x for x in range(1,11) if x%2==0]
print(L2)

L3=[m+n for m in 'ABC' for n in 'XYZ']
print(L3)

import os
L4=[d for d in os.listdir('.')]
print(L4)

L5 = ['Hello', 'World', 18, 'Apple', None]
 
L6=[s.lower() for s in L5 if isinstance(s,str)]
print(L6)
 