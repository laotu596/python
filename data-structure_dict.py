#分析nginx 日志脚本

import  sys.os.time
import datetime
import  pymysql

#数据库连接信息
connect = pymysql.Connect(
    host = 'localhost',
    port = 3306,
    user = 'root'
    passwd = 'xxxx'
    db = 'logs'
)

cursor = connect.cursor()

#当前时间
addtime = datetime.datetime.now()

#初始化字典
dict_list = {}

with open('access.log') as logfin:
    for line in logfin:
        arr = line.split(' ')
        ip = arr[0]
        url = arr[6]
        status = arr[8]
        # 字典get 方法，对取得key得值加1，第一次循环由于字典为空，指定得key 不存在返回默认值0，因此读第一行日志时，统计结果为1
        dict_list[(ip,url,status)] = dict_list.get((ip,url,status),0)+1
    #从字典中去除key和value，存在列表中，由于字典得key 比较特殊是有多个元素构成得元组，通过索引k[x] 得方式去除key得每个元素
    ip_list = [(k[0],k[1],k[2],v,addtime) for k,v in dict_list.items()]

sql = "insert into loginfo values(%s,%s,%s,%s,%s)"
cursor.excutemany(sql,ip_list)
connect.commit()