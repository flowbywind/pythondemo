import sqlite3

conn=sqlite3.connect("chinahadoop.db")

c=conn.cursor()

books=[(1,1,'cook recipe',3.12,1),
       (2,3,'python',5.12,1),
       (3,4,'AI',11.11,2)
       ]

c.execute("insert into category VALUES (1,1,'kitchen')")

c.execute("insert into category values(?,?,?)",(2,2,'compute'))

c.executemany("INSERT INTO book values (?,?,?,?,?)",books)

conn.commit()
conn.close()
