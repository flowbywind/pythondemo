import requests
import requests.exceptions
r=requests.get("http://www.baidu.com")
print(r.content.decode("UTF8"))
print(r.text)
r=requests.post("http://www.baidu.com")
print(r.status_code)
payload={'key1':'values','key2':'value2'}
r=requests.get("http://httpbin.org/get",params=payload)
print(r.url)
print("this is cookie",len(r.cookies))
try:
    requests.get("http://www.baidu.com",timeout=0.001)
except requests.exceptions.RequestException:
    print("this is timeout")
else:
    print("no exception")
finally:
    print("this is over")



r=requests.get("https://github.com/timeline.json")
print(r.text)
print(r.headers)