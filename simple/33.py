# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义对象
class User(Base):
    # 表名
    __tablename__ = 'user'

    # 表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()

# 创建新User对象
new_user = User(id='1', name='qix')

# 添加到session
session.add(new_user)

# 提交即保存到数据库
session.commit()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
user = session.query(User).filter(User.id=='1').one()

# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)

# 关闭session
session.close()

### 一对多 对应关系定义

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # 一对多
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # “多”的一方的book表是通过外键关联到user表的
    user_id = Column(String(20), ForeignKey('user.id'))