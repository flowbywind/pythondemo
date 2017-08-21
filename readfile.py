import os.path
import xlrd,sys



Filename='D:\\123.xlsx'
if not os.path.isfile(Filename):
    raise (NameError, "%s is not a valid filename" % Filename)
print("it ok")
bk=xlrd.open_workbook(Filename)
skxrange=range(bk.nsheets)
print(skxrange)

for x in skxrange:
    p=bk.sheets()[x].name.encode('utf-8')
    print (p.decode('utf-8'))
    p1=bk.sheets()[x].name
    print(p1)

