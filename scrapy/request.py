import requests

#发送请求
response = requests.get('http://httbin.org.get')
print(response.text)
#请求头
print(response.headers)
#请求状态码
print(response.status_code)

#添加请求头进行请求
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
response = requests.get('http://httbin.org.get')
print(response.headers)
print(response.text)

#进行带参数的post请求
data = {'name':'june'.'password':123456}
response = requests.get('http://httbin.org.get',params=data)
print(response.text)

#进行post请求
data = {'name':'june'.'password':123456}
response = requests.post('http://httbin.org.get',data=data.headers=headers)
print(response.text)
#还可以进行put、delete请求等

#解析json
j = response.json()
print(type(j),j)

#从网上读取二进制数据，比如图片
response = requests.get('https://www.baidu.com/img/bd_logo1.png', headers=headers)
#这个是直接获取字节码
print(response.content)
#这个是获取解码后的返回内容
print(response.text)

#用文件把图片下载下来
with open('baidu.png','wb') as f:
    f.write(response.content)
    print('下载完毕')

#请求成功的状态码
print(request.codes.ok)

#上传文件
files = {'picture':open('baidu.png','rb')}
response = requests.post('http://httpbin.org/post',files=files)
print(response.text)

#获取cookie
response = requests.get('http://www.baidu.com')
for k,v in response.coolies.items():
    print(k,'=',v)

#用会话来保持登录信息
session = request.session()
reponse = session.get('http://httpbin.org/cookies/set/number/123456')
print(response.text)

#证书验证
response  = requests.get('http://www.12306.cn',verify=False)
print(response.status_code)