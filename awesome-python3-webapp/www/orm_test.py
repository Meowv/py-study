# -*- coding: utf-8 -*-

__author__ = '阿星Plus'

'''
orm test
'''

import orm
import asyncio
from models import User, Blog, Comment, next_id

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='ABCdef123456', db='awesome')

    u = User(name='qix', email='123@meowv.com', passwd='123456', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()