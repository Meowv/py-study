# 让对象支持上下文管理

from telnetlib import telnetlib
from sys import stdin, stdout
from collections import deque

class TelnetClient(object):
    def __init__(self, addr, port=23):
        self.addr = addr
        self.port = port
        self.tn = None

    def start(self):
        self.tn = Telnet(self.addr, self.port)
        self.hidtory = deque()

        t = self.tn.read_until('login: ')
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)

        t = self.tn.read_until('password: ')
        if t.startwith(user[:-1]): t = t[len(user) + 1:]
        stdout.write(t)
        self.tn.write(stdin.readline())

        t = self.tn.read_until('$ ')
        stdout.write(t)
        while True:
            input = stdin.read()
            if not input:
                break
            self.hidtory.append(input)
            self.tn.write(input)
            t = self.tn.read_until('$ ')
            stdout.write(t[len(input) + 1:])

    def cleanup(self):
        pass

    def __enter__(self):
        self.tn = Telnet(self.addr, self.port)
        self.hidtory = deque()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('In __exit__')

        self.tn.close()
        self.tn = None
        with open(self.addr + '_history.txt', 'w') as f:
            f.writelines(self.hidtory)
        return True

with TelnetClient('127.0.0.1') as client:
    client.start()

print('end')