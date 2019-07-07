import pymysql

conn = pymysql.connect(host='localhost',user='root',password='123456',database='pydemo',port=3306)
cursor = conn.cursor()

# 删除数据
sql = """
    delete from user where id = 5
"""
cursor.execute(sql)
conn.commit()

# 更新数据
sql = """
    update user set username='spider' where id = 1
"""
cursor.execute(sql)
conn.commit()

conn.close()