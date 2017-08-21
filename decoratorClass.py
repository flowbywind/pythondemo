# 类装饰器

def decor(aClass):
    class newClass:
        def  __init__(self,age):
            print("new class init")
            self.total_display=0
            self.wrapped=aClass(age)
        def display(self):
            self.total_display+=1
            print("total display",self.total_display)
            self.wrapped.display()
    return newClass

@decor
class Bird:
    def  __init__(self,age):
        self.age=age
    def display(self):
        print("my age is ",self.age)

ealgelord=Bird(5)

for i in range(3):
    ealgelord.display()