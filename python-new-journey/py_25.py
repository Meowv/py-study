# 使用临时文件

from tempfile import TemporaryFile, NamedTemporaryFile

help(TemporaryFile)
help(NamedTemporaryFile)

f = TemporaryFile()
f.write(b'abcdef' * 1000)

f.seek(0)
print(f.read(100))

ntf = NamedTemporaryFile(delete=False)
print(ntf.name)