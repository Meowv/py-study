import pymysql

conn = pymysql.connect(host='localhost',user='root',password='123456',database='pydemo',port=3306)
cursor = conn.cursor()

# sql = """
#   insert into user(id,username,age, password) values(1, 'aaa', 18, '123456')
# """
# cursor.execute(sql)
# conn.commit()

sql = """
    insert into user(id,username,age, password) values(NULL, %s, %s, %s)
"""

username = 'spider'
age = 21
password = 12345

cursor.execute(sql, (username,age,password))
conn.commit()

conn.close()