import  pymysql

conn = pymysql.connect(host='localhost',
                              user='shurli',
                              passwd='shurli@2018',
                              port=3306,
                              db="spiders"
                       )

cursor = conn.cursor()
cursor.execute('select version()')
data = cursor.fetchone()
print('Datebase version:',data)
#建立数据库
#cursor.execute("create database spiders default character set utf8")

#建立数据表
#sql = 'create table if not exists students(id varchar(255)not null,name varchar(255)not null,age int not null,primary key(id))'

#插入数据
id = '20120001'
user = 'Bob'
age = 20
#sql = 'insert into students(id,name,age)values(%s,%s,%s) '

#更新数据
#sql = 'update students set age = %s where name = %s'

#查询数据
sql = 'select * from students'
#数据得一致性
try:
#    cursor.execute(sql,(25,'Bob'))
    cursor.execute(sql)
    one = cursor.fetchone()
    print('One:',one)
    print(list(one))
#    conn.commit()
except:
    conn.rollback()


#cursor.execute(sql)
conn.close()