import pymysql

conn = pymysql.connect(host='localhost',user='root',password='123456',database='pydemo',port=3306)
cursor = conn.cursor()

cursor.execute('select 1')
result = cursor.fetchone()
print(result)

conn.close()