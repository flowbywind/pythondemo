import time,pymysql

conn=pymysql.connect(host="localhost",port=3306, user="root",passwd="1234",db="test",charset="utf8")
cursor=conn.cursor()

sql="drop table if EXISTS USER "
cursor.execute(sql)

sql='''
create table if not exists user (
name varchar(128) primary key,
created int (12)
)
'''
cursor.execute(sql)

sql="insert into user(name,created) values (%s,%s)"
param=('aaa',int(time.time()))
n=cursor.execute(sql,param)
print("insert",n)

sql='''
insert into user(name,created) values (%s,%s)
'''
param=(("bbb",int(time.time())),("ccc",22),("ddd",33))
n=cursor.executemany(sql,param)
print("execute many",n)

sql="update user set name=%s where name='aaa'"
param=("zzz",)
n=cursor.execute(sql,param)
print("update",n)

sql="select * from user"
n=cursor.execute(sql)
for row in cursor.fetchall():
    print("行",row)
    for r in row:
        print("列",r)

sql="delete from user where name=%s"
param=("bbb",)
n=cursor.execute(sql,param)
print("delete ",n)

sql="select * from user"
n=cursor.execute(sql)
print(cursor.fetchall())
cursor.close()
conn.commit()#提交
conn.close() #关闭连接

