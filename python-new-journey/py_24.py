# 访问文件的状态

import os
import stat

path = 'python-new-journey/files/log.txt'

s1 = os.stat(path)
print(s1)

print(stat.S_ISDIR(s1.st_mode))
print(stat.S_ISREG(s1.st_mode))
# ...

print(s1.st_mode & stat.S_IRUSR)
print(s1.st_mode & stat.S_IXUSR)

print(s1.st_atime)

import time
print(time.localtime(s1.st_atime))

print(s1.st_size)

print(os.path.isdir(path))
print(os.path.islink(path))
print(os.path.isfile(path))
print(os.path.getatime(path))
print(os.path.getmtime(path))
print(os.path.getctime(path))
print(os.path.getsize(path))