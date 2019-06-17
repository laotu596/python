import requests
from bs4 import BeautifulSoup



url = 'https://book.douban.com/'
response = requests.get(url)
Text = response.txt
#上面的也可以合并为下面一句语句

response = requests.get('https://book.douban.com/').text
#print(reponse)

#创建bs对象(lxml 为python中html 的解析器)
soup = BeautifulSoup(response,'lxml')
print(soup)
pring(soup.prettify())                                     #使用prettify()格式化显示输出

#得到一个BeautifulSoup对象后，一般通过BeautifulSoup类的基本元素来提取html中的内容
#tag                 标签，最基本的信息组织单位，分别用<>和</>标明开头和结尾
#name                标签的名字,<p>...</p>的名字是'p' 格式：<tag>.name
#Attributes          标签的属性，字典形式组织，格式:<tag>.arrts
#NavigableString     标签内非属性字符串,<>...</>中字符串，格式:<tag>.sring
#Commnet             标签内字符串的注释部分，一种特殊的Commnet类型


print(soup.title)                                   #获取html的title标签的信息
print(soup.a)                                       #获取html的a标签的信息(soup.a默认获取第一个a标签，想获取全部就用for循环取遍历)
print(soup.a.name)                                  #获取a标签的名字
print(soup.a.parent.name)                           #a标签的父标签
print(soup.a.parent.parent.name )                   #a标签的父标签的父标签的名字


print(tyrp(soup.a))                                  #查看a标签的类型
print(soup.a.attrs)                                  #获取a标签的所有属性
print(type(soup.a.attrs))                            #查看a标签属性的类型
print(soup.a.attrs['class'])                        #通过字典的方式获取a标签的class属性
print(soup.a.attrs['href'])                         #通过字典的方式获取a标签的href 属性


print(soup.a.string())                                #a标签的非属性字符串信息
print(type(soup.a.string))                            #查看标签string字符串的类型
print(soup.p.sring)                                   #p标签的字符串信息

#find_all方法
#常用通过find_all()方法来查找标签元素：<>.find_all(name, attrs, recursive, string, **kwargs) ，返回一个列表类型，存储查找的结果
#name 对标签名称的检索字符串
#attrs 对标签属性值的检索字符串，可以标注属性检索
#recursiv  是否对子孙全部检索，默认True
#string <>...</> 中字符串区域的检索字符串
#find（）方法 和find_all方法一样，只不过这个方法只是查找一个标签

print(soup.find_all('a'))                            #通过find_all()方法查找a标签，返回一个列表类型
print(soup.find_all(['a'],['b'])                    # 把a标签和b标签作为一个列表传递，可以一次找到a标签和b标签

print('href属性为http..的a标签元素是:', soup.find_all('a', href='http://www.icourse163.org/course/BIT-268001'))  # 标注属性检索
print('class属性为title的标签元素是：', soup.find_all(class_='title'))  # 指定属性，查找class属性为title的标签元素，注意因为class是python的关键字，所以这里需要加个下划线'_'
print('id属性为link1的标签元素是：', soup.find_all(id='link1'))  # 查找id属性为link1的标签元素


print(soup.head)  # head标签
print(soup.head.contents)   # head标签的儿子标签，contents返回的是列表类型
print(soup.body.contents)   # body标签的儿子标签
"""对于一个标签的儿子节点，不仅包括标签节点，也包括字符串节点，比如返回结果中的 \n"""




print(len(soup.body.contents))  # 获得body标签儿子节点的数量
print(soup.body.contents[1])   # 通过列表索引获取第一个节点的内容



print(type(soup.body.children))  # children返回的是一个迭代对象，只能通过for循环来使用，不能直接通过索引来读取其中的内容
for i in soup.body.children:   # 通过for循环遍历body标签的儿子节点
    print(i.name)   # 打印节点的名字

for t in soup.find_all('a'):  # for循环遍历所有a标签，并把返回列表中的内容赋给t
      print('t的值是：', t)  # link得到的是标签对象
      print('t的类型是：', type(t))
      print('a标签中的href属性是：', t.get('href'))  # 获取a标签中的url链接

for i in soup.find_all(True):  # 如果给出的标签名称是True，则找到所有标签
    print('标签名称：', i.name)  # 打印标签名称