# 装饰器

def pre_str(pre=""):
    def decor(F):
        def new_F(a,b):
            print(pre,"input:",a,b)
            return F(a,b)
        return new_F
    return decor

@pre_str("hi +")
def  square_sum(a,b):
    return a**2+b**2

@pre_str("hi -")
def square_diff(a,b):
    return a**2-b**2

print(square_sum(3,4))
print(square_diff(3,4))