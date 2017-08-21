import sqlite3

# .db文件在当前目录下 自动创建
conn=sqlite3.connect("chinahadoop.db")
# 获取数据库游标
c=conn.cursor()

# 执行创建表的操作
c.execute('''
CREATE TABLE category
(id int PRIMARY KEY ,sort int,name text)
''')

c.execute('''
CREATE TABLE book
(id int PRIMARY KEY ,
sort int,
name text,
price real,
category int,
FOREIGN KEY (category) REFERENCES category(id)
)
''')
# 保存
conn.commit()
# 关闭数据库连接
conn.close()