import  sys

#sys 模块常见的函数
#sys.argv   实现从程序外部想程序传递参数，在外部向程序内部传递参数
print(sys.argv[0])

##print(sys.argv[1])             #在命令模式下使用，传入参数

#运行
##pyhon sys.py argv1
#输出
#sys.py
#argv1

#sys.version 获取python解释程序的版本信息
print(sys.version)

#sys.path  获取指定模块搜索路径的字符串集合，
print(sys.path)

#sys.platfor  获取当前操作系统平台
print(sys.platform)

#标准输出，写入字符串输出到屏幕
print(sys.stdout.write('please:'))

#标准输入
val = sys.stdin.readline()[:-1]
print(val)
#退出程序，正常退出时exit(0)
sys.exit(0)

