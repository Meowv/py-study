# -*- coding: utf-8 -*-

from collections import ChainMap
import os,argparse

# 缺省参数
defaults = {
    'color':'red',
    'user':'guest'
}

# 命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组成ChainMap
combined = ChainMap(command_line_args,os.environ,defaults)

# 打印参数
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])