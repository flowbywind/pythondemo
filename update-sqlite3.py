import sqlite3


conn=sqlite3.connect("chinahadoop.db")

c=conn.cursor()

c.execute("update book set price=? where id=?",(999,1)) # 更新价格

c.execute("delete from book where id=2") # 删除id=2的行书

c.execute("DROP TABLE book") # 删除表
conn.commit()

conn.close()