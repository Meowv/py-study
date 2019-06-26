# -*- coding: utf-8 -*-

import time,  sys, queue
from multiprocessing.managers import BaseManager

#创建类似的QueueManage
class QueueManage(BaseManager):
    pass

#由于这个QueueManage只从网络上获取Queue,所以注册时只提供名字
QueueManage.register('get_task_queue')
QueueManage.register('get_result_queue')

#连接到服务器...
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
#端口和验证码注意保持与 services 设置的完全一致
m = QueueManage(address=(server_addr,5000),authkey=b'abc')
# 从网络连接：
m.connect()
#获取Queued的对象
task = m.get_task_queue()
result = m.get_result_queue()
#从task队列取任务，并把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n,n))
        r = '%d * %d = %d' % (n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')

#处理结束
print('worker exit...')

