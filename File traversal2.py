import  os


def gci(filepath):
    files = os.listdir(filepath)                  #os.listdir() 得到一定list包含了目录下所有的文件和文件夹
    for fi in files:
        fi_d = os.path.join(filepath,fi)          #os.path.join 获得文件得全路径
#        print(fi_d)
        if os.path.isdir(fi_d):                   #os.path.isdir 判断是不是一个dir
            print(fi_d)
        else:
            print(os.path.join(filepath,fi_d))
gci('E:\\MP3')


