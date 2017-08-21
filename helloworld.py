
print ('helloworld')

l=[1,2,3,4]
print(type(l))
l.append(5)
print(l)
l.pop(4)
print(l)
print(l[1])
l.append(6)
print(l)
print(l[1:4:1])
l.append(9)
l.append(10)
print(l)
print(l[1:6:2])

d={'jim':33,'hmmeimei':30,'lucy':33}
print(d)
print(d.keys())
print(d.values())
print(d.items())
del(d["lucy"])
print(d)
d.clear()
print(d)