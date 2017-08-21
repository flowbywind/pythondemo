import copy
a=[1,2,3,4,['a','b']]

b =a
c=copy.copy(a)
d=copy.deepcopy(a)

a.append(5)
a[4].append('c')

print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)

print(type([]),type(''),type({}),type(0.0),type((1,)))

for i in range(5):
    print(i,end=' ')  # 不用换行

with open('test.txt','w') as fp:
    print('hello world',file=fp)

fp2=open('test2.txt','w')
print('hello world 2',file=fp2)
fp2.close()
