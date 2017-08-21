import urllib.request as req
import  urllib.parse
values={"username":"suifengpiao1989","password":"zz7654321","lt":"LT-1046443-EfVfrFiAOgvKUg9sg5tHb9ifdEQzvO","execution":"e1s1","_eventId":"submit"}

data=urllib.parse.urlencode(values).encode(encoding='UTF8')
request=req.Request("https://passport.csdn.net/account/login;jsessionid=CF6F53B0B0A3BE483746F2FED6267D5A.tomcat1",data)
response=req.urlopen(request)
print(response.read().decode("UTF8"))

