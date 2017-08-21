class Bird(object):
    feather = True;

class Chicken(Bird):
    fly = False
    def  __init__(self,age):
        self.age=age
    def __getattr__(self, item): #查询即时生成的属性
        if item=="adult":
            if self.age>1.0 :
                return True
            else:
                return False
        else:
            print(item)

chick=Chicken(2)

print(Bird.__dict__)
print(Chicken.__dict__)
print(chick.__dict__)

chick.__dict__['age']=3
print(chick.__dict__['age'])
chick.age=10
print(chick.age)

summer=Chicken(2)
print(summer.adult)
summer.age=0.5
print(summer.adult)
print(summer.male)