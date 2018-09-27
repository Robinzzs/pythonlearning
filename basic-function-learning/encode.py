# -*- coding: utf-8 -*-

print('包含中文的str')

ord('A')

chr(66)

a='ABC'.encode('ascii')
print(a)

b='中文'.encode('utf-8')
print(b)

c=a.decode('utf-8')
print(c)
