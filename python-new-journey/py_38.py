# 多线程
# 使用标准库 threading.Thread 创建线程

# 线程间通信
# 使用标准库中 Queue.Queue 它是一个线程安全的队列

# 在线程间进行事件通知
# 使用标准库中 Threading.Event
# 1.等待事件一端调用 wait 等待事件
# 2.通知事件一端调用 set  通知事件

# 使用线程本地数据
# threading.loca 函数可以创建线程本地数据空间，其下属性对每个线程独立存在

# 线程池
# 使用标准库中 concurrent.futures 下的 ThreadPoolExecutor 对象的 submit 和 map 方法可以用来启动线程池中线程执行任务

# 多进程
# 使用标准库中 multiprocessing.Process 它可以启动子进程执行任务操作接口,进程间通信,进程间同步等都与 Threading.Thread 类似