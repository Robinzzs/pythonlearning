# -*- coding: utf-8 -*-

#class MuffleCalculator:
#    muffled = False
#    def calc(self,expr):
#        try:
#            print(eval(expr))
#        except ZeroDivisionError:
#            if self.muffled:
#                print('division by zero is illegal')
#                
#            else:
#                raise
#                
#                
#                
#
#calculator=MuffleCalculator()
#calculator.calc('10/2')
#
#
#calculator.muffled=True
#
#calculator.calc('10/0')


#try:
#    x=input('number:')
#    y=input('number:')
#    print(x/y)
#except ZeroDivisionError:
#    print("the second number cant ber zero")
#except TypeError:
#    print("that wasnt a nubmer, was it?")
    
    
#    
#try:
#    x=input('number:')
#    y=input('number:')
#    print(x/y)
#except (ZeroDivisionError,TypeError) as e:
#    print(e)


while True:
    try:
        x=float(input('x'))
        y=float(input('y'))
        
        print(x/y)
    except(ZeroDivisionError):
        print('invailid input , please try again')
        
    else:
        break
