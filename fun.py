def add(a, b):
    a = a+b
    return a
c = add(1, 3)
print(c)

# 位置传递


def f(a, b, c):
    return a+b+c
print(f(1, 2, 3))

# 关键词传递
d = f(a=1, c=3, b=4)
print(d)

# 参数默认值


def f1(a, b, c=10):
    return a+b+c
print(f1(2, 3, 7))

# 包裹传递 打包成元祖


def func(*name):
    print(type(name))
    print(name)
# 将参数打包成一个传递给参数
func(1, 2, 3, 4)

# 包裹关键字传递  打包成字典


def func1(**name):
    print(type(name))
    print(name)
    print(name.keys())

func1(a=1, b=2, c=3)


def func3(a, b, c):
    print(a, b, c)

a = (1, 2, 3)
func3(*a)  # 解包裹

b = {'b': 28, 'a': 10, 'c': 83}
func3(**b)  # 关键字解包裹


# 先位置 后关键字传递 包裹位置 包裹关键字
