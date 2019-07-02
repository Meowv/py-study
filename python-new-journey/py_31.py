# 派生内置不可变类型并修改其实例化行为

# 实现 __new__ 修改实例化行为

class IntTuple(tuple):
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x,int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)

    def __init__(self, itetable):
        super(IntTuple,self).__init__(itetable)

t = IntTuple([1,-1,'abc',6,['x','y'], 3])
print(t)