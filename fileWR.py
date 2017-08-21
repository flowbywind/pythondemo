f=open("fileoperate.txt","w")
f.write("ddd\n")
f.write("eee")

with open("fileoperate.txt","r") as f:
    print(f.readline())
