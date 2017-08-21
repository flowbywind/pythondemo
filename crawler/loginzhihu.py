import urllib.parse as urlcode
import urllib.request
url="https://www.zhihu.com/#signin"
url="http://www.baidu.com"
values={"account":"18520789089","password":"zz7654321"}
user_agent='Mozilla/5.0 (Windows NT 10.0) '
headers={'User-Agent':user_agent}
data=urlcode.urlencode(values).encode("UTF8")
request=urllib.request.Request(url,data,headers)
response=urllib.request.urlopen(request)
print(response.read().decode("UTF8"))
print(response.status_code)
print(response.headers['content-type'])
