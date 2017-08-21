class Me(object):
    def test(self):
        print("hello")

def new_test():
    print("new hello")

me=Me()

print(hasattr(me,"test"))

print(getattr(me,"test"))

print("before:",me.test())

print(setattr(me,"test",new_test))


print(delattr(me,"test"))

print("after:",me.test())

print(isinstance(me,Me))

print(issubclass(Me,object))

f=open("test.txt","r")
res=f.readlines()
for i in res:
    print(i)



