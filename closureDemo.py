# 闭包

def line_conf(a,b):
    def line(x):
        return a*x+b
    return line

line1=line_conf(1,1)
line2=line_conf(4,5)

print(line1(5))
print(line2(10))
print(line1.__closure__)
print(len(line1.__closure__))
print(line1.__closure__[0].cell_contents)