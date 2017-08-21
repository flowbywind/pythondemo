from datetime import  *
import time

print('datetime.max'+str(datetime.max))
print('datetime.min'+str(datetime.min))
print("today"+str(datetime.today()))
print('now'+str(datetime.now()))
print("utcnow()"+str(datetime.utcnow()))
print('time.time'+str(time.time()))
print('fromtimestamp'+str(datetime.fromtimestamp(time.time())))
print('utcfromtimestamp(tmstmp)'+str(datetime.utcfromtimestamp(time.time())))
d=date(2012,9,2)
print(d)

dt=datetime.now()
print(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.minute,dt.weekday(),dt.isocalendar())

print(dir(tuple))

print("nihao".__add__('beijing'))
print(1.1.__mul__(8))
print(len([1,2,3,4,5]))
print([1,2,3,4,5].__len__())
a=[1,2,3,4,5]
print(a[3])
print(a.__getitem__(3))
a[0]=0
print(a)
a.__setitem__(0,10)
print(a)

class A(object):
    def  __call__(self,a):
        return a+10

b=A()
print(b(1))
print(dir(A))
c=map(b,[1,2,34,5,6])
for i in c:
    print(i,end=',')

print(big(3))
