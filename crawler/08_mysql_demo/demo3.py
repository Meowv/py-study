import pymysql

conn = pymysql.connect(host='localhost',user='root',password='123456',database='pydemo',port=3306)
cursor = conn.cursor()

# fetchone
sql = """
    select username,age from user where id = 2
"""
cursor.execute(sql)
result = cursor.fetchone()
print(result)

# fetchall
sql = """
    select * from user
"""
cursor.execute(sql)
result = cursor.fetchall()
print(result)

# fetchmany
sql = """
    select * from user
"""
cursor.execute(sql)
result = cursor.fetchmany(2)
print(result)

conn.close()