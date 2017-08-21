import operator


print(abs(-2),round(2.3),pow(3,2),divmod(9,7),max([2,4,6,8]),min(2,4,6,8))

print(sum([2,3,4]),sum((1,3,5)),sum(range(5)))

print(operator.gt(3.1,3.2))

print(int("333"))

print(float(3))

print(divmod(float(9), float(7)))

print(float(9)/float(7))
print(int(9/7))

print(complex(1,2))  # 返回复数

print(ord('A'),chr(65),bool(0))
print(all([True,2,'dd']))
print(any([0,'',[],'ddd']))
print(sorted([1,3,8,4,2]))
for x in reversed([1,3,8,4,2]):
    print(x)

print(list((1,4,3)))
print(tuple([1,4,3]))
print(dict(a=3,b='hi',c=[12,3,3]))

print(globals())
print(locals())
print(input('please input something:'))

def p(nums):
    for x in nums:
        print(x)

nums=range(2,20)
for i in nums:
    nums=filter(lambda x:x==i or x%i,nums)
    print(list(nums))

print(list(nums))
