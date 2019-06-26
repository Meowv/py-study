# -*- coding: utf-8 -*-

import asyncio

@asyncio.coroutine
def hello():
    print('Hello World!')
    # 异步调用asyncio.sleep(1)
    print('Hello again!')

# 获取EventLoop
loop = asyncio.get_event_loop()

# 执行coroutine
loop.run_until_complete(hello())
loop.close()