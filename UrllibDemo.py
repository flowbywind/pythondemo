import  urllib.request

# urlopen(url,data,timeout)
# url:url  data：要传送的数据 timeout:超时时间
response=urllib.request.urlopen(url="http://www.baidu.com",timeout=1)
print(response.read())

request=urllib.request.Request("http://www.baidu.com")
response=urllib.request.urlopen(request)
print(response.read())