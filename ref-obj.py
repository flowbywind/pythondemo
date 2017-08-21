from sys import getrefcount
import  gc
a=[1,2,3]
print(getrefcount(a))
b=[a,a]
print(getrefcount(a))


a = "hello  world"
b = "hello  world"

print(id(a))
print(id(b))

a = 3
b = 3

print(id(a))
print(id(b))

class from_obj(object):
    def  __init__(self,to_obj):
        self.to_obj=to_obj

b=[1,2,3]
a=from_obj(b)
print(id(a.to_obj))
print(id(b))

# python generation分代回收策略 0,1,2

print(gc.get_threshold())

#　独立引用环的问题

a=[]
b=[a]
a.append(b)

del a
del b
