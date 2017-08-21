a=1

# 值传递
def change_integer(c):
    c=c+1
    print(id(c))
    return c

print(change_integer(a))
print(a)
print("out a:",id(a))
#引用传递
b=[1,2,3]

def change_list(b):
    print("in b:",id(b))
    b[0]=b[0]+1
    return b

print(change_list(b))
print(b)
print("out b:",id(b))
