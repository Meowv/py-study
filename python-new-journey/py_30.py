# 为创建大量实例节省内存

# 定义类的__slots__属性

class Player(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level

class Player2(object):
    __slots__ = ['uid', 'name', 'status', 'level']
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level