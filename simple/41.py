import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=localhost;DATABASE=Meowv_Blog;UID=sa;PWD=123456')

cursor = conn.cursor()
cursor.execute('select getdate()')
row = cursor.fetchone()
print(row)

conn.close()