# 函数即对象 函数有自己的属性
# Lambda生成一个函数对象
# 函数可作为参数传递
from functools import  reduce
import operator

func = lambda a, b: a + b

print(func(1, 2))


def sum1(f, x, y):
    print('--- in sum function')
    return f(x, y)

print(sum1(func, 2, 8))

b = {'dd': 3, 'dds': 5}
print(dir(b))  # 查看对象的方法列表

print(dir(sum1))

print(help(list))  # 帮助查看对象

print(len(b))

print(len('dfdfsdfsd'))

print(help(zip))

ll = [1]
i = iter(ll)
print(i.__next__())

print(help(map))

d=map((lambda a: a**2), [1, 2, 3])
for x in d:
    print(x)

print(help(filter))


def big(x):
    if x > 5:
        return True
    else:
        return False

r=filter(big,[4,5,6])
for x in r:
    print(x)

print(help(reduce))

x=reduce((lambda x, y: x+y),[1, 3, 5, 7])
print(x)

