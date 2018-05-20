# -*- coding: utf-8 -*-

#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
#所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

#try:
#    f = open('/path/to/file', 'r')
#    print(f.read())
#finally:
#    if f:
#        f.close()

#但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

#with open('/path/to/file', 'r') as f:
#    print(f.read())

#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；
#如果是配置文件，调用readlines()最方便：
#
#for line in f.readlines():
#    print(line.strip()) # 把末尾的'\n'删掉



#file-like Object
#
#像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
#除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承
#，只要写个read()方法就行。
#
#StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

#二进制文件
#
#前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，
#用'rb'模式打开文件即可：
#
#>>> f = open('/Users/michael/test.jpg', 'rb')
#>>> f.read()
#b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节

#字符编码
#
#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
#
#>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
#>>> f.read()
#'测试'
#
#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些
#非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
#
#>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')



#写文件
#
#写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写
#二进制文件：
#
#>>> f = open('/Users/michael/test.txt', 'w')
#>>> f.write('Hello, world!')
#>>> f.close()
#
#你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，
#操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
#只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果
#是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
#
#with open('/Users/michael/test.txt', 'w') as f:
#    f.write('Hello, world!')
#
#要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。
#
#细心的童鞋会发现，以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入
#一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。

#fpath = r'C:\Users\zzs\OneDrive\pythonlearning\bbbbb.txt'
#with open(fpath, 'a') as f:
#    #s = f.read()
#    f.write('add something!!!')
##    s = f.read()
##    print(s)
#    
#with open(fpath, 'r') as f:
#    #s = f.read()
##    f.write('add something!!!')
#    s = f.read()
#    print(s)

fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
    
    



