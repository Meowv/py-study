# 自定义参数的装饰器

from inspect import signature

def typeassert(*ty_args, **ty_kargs):
    def decorator(func):
        sig = signature(func)
        btypes = sig.bind_partial(*ty_args, **ty_kargs).arguments
        def wrapper(*args, **kargs):
            for name, obj in sig.bind_partial(*args, **kargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError('%s must be %s' % (name, btypes[name]))
            return func(*args, **kargs)
        return wrapper
    return decorator

@typeassert(int ,str, list)
def f(a,b,c):
    print(a,b,c)

print(f(1,'abc', [1,2,3]))
print(f(1, 2, [1,2,3]))