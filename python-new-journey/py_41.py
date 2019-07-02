# 为被装饰的函数保存元数据

from functools import update_wrapper, wraps,WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES

def mydecorator(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        print('In wrapper')
        func(*args, **kargs)
    return wrapper

@mydecorator
def example():
    print('In example')

print(example.__name__)
print(example.__doc__)