# 设置文件的缓冲 

f =  open('python-new-journey/files/test1.txt', 'w', buffering=2048)

f.write('+' * 1024)
f.write('+' * 1024)
f.write('-' * 2)

f =  open('python-new-journey/files/test2.txt', 'w', buffering=1)

f.write('abcd')
f.write('1234')
f.write('\n')
f.write('xyz')

# f =  open('python-new-journey/files/test3.txt', 'w', buffering=0)
# f.write('a')
# f.write('b')
# f.write('c')