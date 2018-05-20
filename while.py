#! /usr/bin/env python2.7

"""This script parse the content of a xml file"""

# name = ''
# while not name :
#     name = raw_input('Please enter your name: ')

# print 'hello, %s' %name

# words = ['this','is','an','ex','parrot']
# for word in words :
#     print word

# for number in range(1,101):
#     print number

# names=['anne','beth','george','damon']
# ages=[12,45,32,102]

# for name,age in zip(names,ages):
#     print name, 'is',age,'years old'

# from math import sqrt
# for n in range(99,0,-1):
#     root=sqrt(n)
#     if root == int(root):
#         print n
#         break

# while True:
#     word = raw_input('Enter a word:')
#     if not word: break

#     print 'the word is '+word


from math import sqrt

for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
else:
    print "don't find it"







