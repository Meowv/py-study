# 读写文本文件

f = open('python-new-journey/files/hello.txt', 'wt', encoding='utf8')

f.write('读写文本文件测试')

f.close()

f = open('python-new-journey/files/hello.txt', 'rt', encoding='utf8')

s = f.read()
print(s)