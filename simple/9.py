# -*- coding: utf-8 -*-

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://youzy.cn')) as page:
    for line in page:
        print(line)

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()