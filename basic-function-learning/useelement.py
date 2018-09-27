# -*- coding: utf-8 -*-


def fn(self, name='world'):
    print('Hello, %s' % name)
    
    
Hello = type('Holle', (object,), dict(hello=fn))

h = Hello()

h.hello()

print(type(Hello))

print(type(h))


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
    
class Mylist(list, metaclass=ListMetaclass):
    pass

L= Mylist()
L.add(1)
print(L)

#class User(Model):
#    
#    id = IntegerField('id')
#    name = StringField('username')
#    email = StringField('passward')
#    
#    
#u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd)
#
#u.save()

    
class Field(object):
    
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
        
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
    
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
        
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
        
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                
        for k in mappings.keys():
            attrs.pop(k)
            
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)
    
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
        
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribut '%s'" % key)
            
    def __setattr__(self, key, value):
        self[key] = value
        
    def save(self):
        fields = []
        params = []
        args   = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__,','.join(fields),','.join(params))
        print('SQL: %s' %sql)
        print('ARGS: %s' % str(args))
        



class User(Model):
    
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('passward')
    
    
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')

u.save()


#ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

#要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
        
        
        
        
        
        
    