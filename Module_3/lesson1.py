from psycopg2 import connect

conn = connect(database='p11_db', user='postgres', password='1111', host='localhost')
cur = conn.cursor()
query = 'select * from students'
cur.execute(query)
s = cur.fetchall()
for i in s:
    print(i)