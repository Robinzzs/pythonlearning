# -*- coding: utf-8 -*-
#!/usr/bin/env python27
'a test module'

__author__ = ' Robinzzs'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('hello, world !')
    elif len(args)==2:
        print('hello, %s'%args[1])
    else:
        print('too many arguments')

if __name__ == '__main__':
    test()
    


    
