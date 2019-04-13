# -*- conding:utf-8 -*-
# @Time    :2019/4/13 15:34
# @Author  :yahs0105
# @FileName:函數.py
# @Ide     :PyCharm

# def f():
#     print('OK')
#
# f()     #調用一定要記得加括號

# def add(x,y):
#
#     print(f'{x}+{y}={x+y}')
#
# add(10,5)
import time

def logger(n):
    time_format = '%Y-%m-%d %x'
    time_current = time.strftime(time_format)

    with open('日誌記錄','a') as f:
        f.write(f'{time_current} end action{n}\n')

def action1(n):
    print('starting action1...')
    logger(n)

def action2(n):
    print('starting action2...')
    logger(n)

def action3(n):
    print('starting action3...')
    logger(n)



action1(11)
action2(22)
action3(33)



