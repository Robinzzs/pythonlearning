# -*- coding: utf-8 -*-

#assert


#def foo(s):
#    n = int(s)
#    assert n != 0, 'n is zero!'
#    return 10 / n
#
#def main():
#    foo('0')
#    
#main()

#程序中如果到处充斥着assert，
#和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert
# python -O err.py



#logging

#import logging
#
#logging.basicConfig(level=logging.INFO)
#
#s = '0'
#n = int(s)
#logging.info('n = %d' % n)
#print(10 / n)
#



# pdb
# python -m pdb err.py
#s = '0'
#n = int(s)
#print(10 / n)



# pdb.set_trace()
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)