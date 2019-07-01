# 处理二进制文件

f = open('python-new-journey/files/love.mp4', 'rb')

info = f.read(100)
print(info)

import struct
import array

# ...

# open函数以二进制模式打开文件，指定mode参数为 'b'
# 二进制数据可以用readinto 读入到提前分配好的buffer中，便于数据处理
# 解析二进制可以用struct模块的unpack方法