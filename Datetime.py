import datetime,time

#datetime 模块定义了下面的几个类
#datetime。date  表示日期的类，常用的属性有year、month、day；
#datetime.time   表示时间的类，常用的属性有hour、minute、second、microsecond
#datetime.datetime  表示日期时间
#datetimne.timedalta   表示时间间隔，即俩个时间点之间的长度
#datetime。tzinfo   与时区有关的相关信息


#datetime.date 类
#datetime.date(year,month,day)

t = time.time()
print(datetime.date.today())                              #获取当前本地日期的时间对象
#print(datetime.datetime.now())                            #同上
print(datetime.date.fromtimestamp(t))                     #根据时间戳，返回时间对象
print(datetime.date.today().year)                         #获取年份
print(datetime.date.today().month)                        #获取月份
print(datetime.date.today().day)                          #获取当月的第几天
print(datetime.date.today().isoweekday())                 #获取时间对象时星期几
print(datetime.date.today().isoformat())                  #获取时间对象的字符串时间，格式 YYYY-MM-DD


#datetime.time  类
#time代表本地一天内的时间
#datetime.time(hour=0,minute=0,second=0,microsecond=0,tzinfo=None,*,fold=0)

print(datetime.time)
print(datetime.time(16,24,15).hour)
print(datetime.time(16,24,15).minute)
print(datetime.time(16,24,15).second)
print(datetime.time(16,24,15).isoformat())
print(datetime.time(16,24,15).strftime('%H:%M:%S'))