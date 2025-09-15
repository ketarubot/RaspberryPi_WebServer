import pymysql

conn = pymysql.connect(host='localhost', user='test', password='test123', db='shopping_db')
cur = conn.cursor()
cur.execute('select * from customer')
rows = cur.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()

