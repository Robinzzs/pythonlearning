# -*- coding: utf-8 -*-

import os


#注意uname()函数在Windows上不提供
print(os.name)
#print(os.uname())
#print(os.environ)
#print(os.environ.get('PATH'))

print(os.path.abspath('.'))



os.mkdir('/Users/zzs/OneDrive/pythonlearning/testdir')

os.rmdir('/Users/zzs/OneDrive/pythonlearning/testdir')

#合并路径
os.path.join('/Users/michael', 'testdir')
#拆分路径
os.path.split('/Users/michael/testdir/file.txt')
#可以直接让你得到文件扩展名
os.path.splitext('/path/to/file.txt')


## 对文件重命名:
#>>> os.rename('test.txt', 'test.py')
## 删掉文件:
#>>> os.remove('test.py')


#幸运的是shutil模块提供了copyfile()的函数，
#你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充


#最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
#
#>>> [x for x in os.listdir('.') if os.path.isdir(x)]
#['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
#
#要列出所有的.py文件，也只需一行代码：
#
#>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
#['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']



#dir -l


import time, os
# 时间戳格式转换
def timenum2str(timenum):
    # print('timenum = ', timenum)
    t = time.localtime(timenum)
    # print('t = ', t)
    return time.strftime('%Y-%m-%d %H:%M', t)

# 获取文件的修改时间
def getTime(filepath):
    t = os.path.getmtime(filepath)
    return timenum2str(t)

# 获取文件大小（单位：字节）
def getSize(filepath):
    s = str(os.path.getsize(filepath))
    while True:
        if len(s) < 5:
            s = ' ' + s
        else:
            break
    return s

if __name__ == '__main__':
    for f in [x for x in os.listdir('.')]:
        print(getSize(f), getTime(f), ' ', f)
        
        
        
        
        
#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
#并打印出相对路径。
        
        
import os

def find(keywords,path=os.path.abspath('.')):
    for x in os.listdir(path) :
        if os.path.isfile(x) and os.path.splitext(x)[0].find(keywords)!=-1:
            

        #print(p)
            print('Find file:%s,Path:%s'%(x,path))

        elif os.path.isdir(x):
            try:
                find(keywords,os.path.join(path,x))
            except PermissionError:
                pass
        return


find('while.py')
        