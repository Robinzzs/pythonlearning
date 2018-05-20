# -*- coding: utf-8 -*-

class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.__gender = None
        
    
    def get_gender(self):
        return self.__gender
    
    def set_gender(self,gender):
        if gender in ('male', 'female'):
            self.__gender = gender
        else:
            raise ValueError('gender error')
        
        
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())


bart = Student('Bart','male')
if bart.get_gender() != 'male':
    print('fail')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        
        print('fail')
    else:
        print('success')

