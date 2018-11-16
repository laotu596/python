import os

#遍历文件
#文件遍历模块以及功能说明
#os.walk() 方法用于通过在目录数种游走输出在目录中的文件名,向上或者向下
#os.walk() 语法格式如下
#os.walk(top,topdown=True,oneroor=None,followlinks=False)

#1、第一个参数fpath 时遍历打印所有的文件路径
#2、第二个参数dirname 是遍历打印都有的文件夹名称
#3、第三个参数fnames
path = r"E:\MP3"                                   #查找文件的路径
for fpath,dirname,fnames in os.walk(path):
    print(fpath)                                     #打印所有的文件夹路径
    print(dirname)                                   #所有的文件夹名
    print(fnames)                                    #所有的文件名

#遍历所有的文件
#遍历查找文件内所有的子文件
#用endswith判断查找后置是.mp结尾的

def get_files(path='e:\MP3',rule=".mp3"):
    all = []
    for fpath,dirs,fs in os.walk(path):
        for f in fs:
            filename = os.path.join(fpath,f)      #join 函数起到字符串连接功能；此处为文件路径和文件名连接到一块
            if filename.endswith(rule):
                all.append(filename)
    return all
if __name__ == "__main__":
    b = get_files(r"E:\MP3")
    for i in b:
        print(i)