# -*- coding: utf-8 -*-

d={'mick':99,'jack':88}
print(d['mick'])

a='tom' in d
print(a)

d.pop('jack')
print(d)

d['bb']=90
print(d)

#key=[33,66]
#d[key]='a list'

s = set([1,2,3])
print(s)

s.add(6)
print(s)
s.remove(3)
print(s)


s1=set([2,3,1,2])
s2=set([4,3,5,6])

s3=s1&s2   #交∩
print(s3)
s4=s1|s2   #并∪
print(s4)


a=['c','d','a']
a.sort()
print(a)

a='acd'
b=a.replace('a','d')
print(a,b)

