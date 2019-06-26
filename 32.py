# -*- coding: utf-8 -*-

# 导入MySQL驱动
import mysql.connector

# 连接到MySQL数据库
conn = mysql.connector.connect(host='', port=3306, user='', password='', database='')
cursor = conn.cursor()

# 创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一行记录，注意MySQL的占位符是%s
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'qix'])

print(cursor.rowcount)

# 查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()