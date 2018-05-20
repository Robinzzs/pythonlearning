# -*- coding: utf-8 -*-

class Class:
    def method(self):
        print('i have a self!')
        


def function():
    print('i dont ... ')
    
    
    
    
instance = Class()
instance.method()

instance.method = function

instance.method()


class Bird:
    song='squaawk'
    def sing(self):
        print(self.song)
        
bird=Bird()
bird.sing()

birdsong=bird.sing
birdsong()


class Secretive:
    
    def __inaccessible(self):
        print('bet you can see me  ')
        
    def accessible(self):
        print('the secret is ')
        self.__inaccessible()
        
s= Secretive()
#s.__inaccessible()
s.accessible()

s._Secretive__inaccessible()
