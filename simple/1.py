# -*- coding: utf-8 -*-

# class Student(object):
#     # __init__ 第一个参数永远是 self    
#     def __init__(self, name, gender):
#         self.__name = name
#         self.__score = gender

#     def print_score(self):
#         print('%s: %s' % (self.__name,self.__score))

#     def get_name(self):
#         return self.__name

#     def get_score(self):
#         return self.__score

#     def set_score(self,score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')

# qix = Student("qix",100)
# qix.print_score()


# class Animal(object):
#     def  run(self):
#         print('Animal is running...')

# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')
#     def eat(self):
#         print('Eating meat...')

# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')
#     def eat(self):
#         print('Eating shit...')


# dog = Dog()
# dog.run()
# dog.eat()

# cat = Cat()
# cat.run()
# cat.eat()

# a = list() # a是list类型
# b = Animal() # b是Animal类型
# c = Dog() # c是Dog类型

# isinstance(a,list)
# isinstance(b,Animal)
# isinstance(c,Dog)

# isinstance(c,Animal)

# def run_twice(animal):
#     animal.run()
#     animal.run()

# run_twice(Animal())
# run_twice(Dog())
# run_twice(Cat())

# class Tortoise(Animal):
#     def run(self):
#         print('Tortoise is running slowly...')

# run_twice(Tortoise())



# class Timer(object):
#     def run(self):
#         print('Start...')



# class Student(object):

#     def get_score(self):
#         return self._score
    
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# s = Student()
# s.set_score(60)
# s.get_score()

# s.set_score(999)

# class Hello(object):
#     def hello(self,name='world'):
#         print('Hello, %s.' % name)




# class Field(object):

#     def __init__(self,name,column_type):
#         self.name = name
#         self.column_type = column_type

#     def __str__(self):
#         return '<%s:%s>' % (self.__class__.__name__,self.name)

# class StringField(Field):

#     def __init__(self,name):
#         super(StringField,self).__init__(name,'varchar(100)')

# class IntegerField(Field):

#     def __init__(self,name):
#         super(IntegerField,self).__init__(name,'bigint')

# class ModelMetaclass(type):

#     def __new__(cls,name,bases,attrs):
#         if name == 'Model':
#             return type.__new__(cls,name,bases,attrs)
#         print('Found model: %s' % name)
#         mappings = dict()
#         for k,v in attrs.items():
#             if isinstance(v,Field):
#                 print('Found mapping: %s' % (k,v))
#                 mappings[k] = v
#         for k in mappings.keys():
#             attrs.pop(k)
#         attrs['__mappings__'] = mappings
#         attrs['__table__'] = name
#         return type.__new__(cls,name,bases,attrs)

# class Model(dic,metaclass=ModelMetaclass):

#     def __init__(self,**kw):
#         supper(Model,self).__init__(**kw)

#     def __getattr__(self,key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'" % key)

#     def __setattr__(self,key,value):
#         self[key] = value

#     def sava(self):
#         fields = []
#         params = []
#         args = []
#         for k,v in self.__mappings__.items():
#             fields.append(v.name)
#             params.append('?')
#             args.append(getattr(self,k,None))
#         sql = 'insert into %s (%s) value (%s)' % (self.__table__,',').join(fields),','.join(params)
#         print('SQL: %s' % sql)
#         print('ARGS: %s' % str(args))


# class User(Model):
#     # 定义类的属性到列的映射
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')

# u = User(id=12345,name='qix',email='hackxing@foxmail.com',password='123')
# u.sava()

# with open('E:/1.txt', 'r', encoding='utf-8') as f:
#     for line in f.readline():
#         print(line.strip())

# with open('E:/1.txt', 'w', encoding='utf-8') as f:
#     f.write('123')

# with open('E:/1.txt', 'a', encoding='utf-8') as f:
#     f.write('123')

# path = r'C:\Windows\system.ini'

# with open(path, 'r') as f:
#     s = f.read()
#     print(s)

# from io import StringIO
# f = StringIO()
# f.write('hello')