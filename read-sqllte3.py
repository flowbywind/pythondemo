
import  sqlite3

newconn=sqlite3.connect("chinahadoop.db")

c=newconn.cursor()

c.execute("select name from category ORDER BY sort")
print(c.fetchone())
print(c.fetchone())

c.execute("select * from book where book.category=1")
print(c.fetchall())

for row in c.execute("select name,price from book order by sort"):
    print(row)