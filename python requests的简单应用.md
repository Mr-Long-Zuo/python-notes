### requests

引入
```
import requests
```

简单请求
```
r = requests.get("http://httpbin.org/get")
r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")
```

带参请求
```
params = {"query" : "东方树叶"}
r = requests.get("https://www.sogou.com/web", params=params)
print(r.text)
```

text和content的区别
* r.text 返回的是unicode的数据
* r.content 返回的是二进制数据（用于图片、文件）
```
r = requests.get("https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png")

with open('1.jpg', 'wb') as f:
    f.write(r.content)
```

内置json函数
```
r = requests.get("http://httpbin.org/ip")
print(r.json()["origin"])
// 103.30.48.250
```

网页状态吗
```
// allow_redirects = False 禁止跳转

r = requests.get("http://httpbin.org/redirect-to?url=http://www.baidu.com", allow_redirects = False)
print(r.status_code)
// 302
```

响应头
```
r = requests.get("http://httpbin.org/get")
print(r.headers)
print(r.headers["Content-Type"])
```

超时设置
```
try:
    r = requests.get("http://github.com", timeout = 0.01)
    print(r)
except:
    print("超时")
```

代理访问
```
proxies = {
    "http" : "http://91.121.162.173:80",
    "https" : "https://60.168.246.71:808"
}

r = requests.get("http://httpbin.org/get", proxies = proxies)
```

请求头内容
```
r = requests.get("http://httpbin.org/get")
print(r.request.headers)
```

自定义请求头
```
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
}
r = requests.get("http://httpbin.org/get", headers = headers)
print(r.request.headers)
```

### 扩展
官方中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
http很不错的测试工具：http://httpbin.org/