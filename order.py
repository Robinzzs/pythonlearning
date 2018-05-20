# -*- coding: utf-8 -*-

l=sorted([36, 5, -12, 9, -21])

print(l)

l2=sorted([36, 5, -12, 9, -21], key=abs)

print(l2)




L=[('Bob',75), ('Adam',95), ('Bart',66), ('Lisa',68)]

#直接排序
L1=sorted(L)
print(L1)
#[('Adam', 95), ('Bart', 66), ('Bob', 75), ('Lisa', 68)]

#取tuple第一个元素，不区分大小写
L2=sorted(L,key=lambda t:t[0].lower())
print(L2)
#[('Adam', 95), ('Bart', 66), ('Bob', 75), ('Lisa', 68)]

#取tuple第二个元素
L3=sorted(L,key=lambda t:t[1])
print(L3)
#[('Bart', 66), ('Lisa', 68), ('Bob', 75), ('Adam', 95)]

#取tuple第二个元素,倒序
L4=sorted(L,key=lambda t:t[1],reverse=True)
print(L4)
#[('Adam', 95), ('Bob', 75), ('Lisa', 68), ('Bart', 66)]

def by_name(t):
    return t[0]

def by_score(t):
    return -t[-1]

L5=sorted(L,key=by_name)        #???????key=abs，即key赋值对应的函数，
                                 #得到对应的关键字key，再对key进行排序，排序key对应的数据
                                 #传入函数
print('L5',L5)    

L6=sorted(L,key=by_score)
print('L6',L6)  



from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))


func=lambda t:t[1]

test=func(('Bob', 75))
print('test',test)
    