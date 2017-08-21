#!/usr/bin/env python
import random
try:
    r=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    print(r**10)
    print(type(r))
    r=r/0
except EOFError:
    print("got it !")
except :
    print("not get")
else:
    print("yes it ok")
finally:
    print("must exe")
print('---the end ----')
print(random.randrange(1,100))
a=[1,2,3,4]
a.reverse()
print(a)
print(a[-1::-1])
print("这是中文")