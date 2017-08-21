import random

a=[12,3,9,0]
a.reverse()
try:
    for x in a:
        print(x)
finally:
    a.reverse()

ab={1:"r",2:"3",3:"dds"}
for i in range(len(ab)-1,-1,-1):
    print(i)

print(random.choice( range(11)))