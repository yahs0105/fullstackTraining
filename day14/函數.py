# -*- conding:utf-8 -*-
# @Time    :2019/4/13 15:34
# @Author  :yahs0105
# @FileName:函數.py
# @Ide     :PyCharm

# def f():
#     print('OK')
#
# f()     #調用一定要記得加括號

# LOW 加法器
# def add(x,y):
#
#     print(f'{x}+{y}={x+y}')
#
# add(10,5)

# 高大尚 加法器
# *args(元組)是一個不定長參數,是一種無命名參數
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)

# import time
#
# def logger(n):
#     time_format = '%Y-%m-%d %x'
#     time_current = time.strftime(time_format)
#
#     with open('日誌記錄','a') as f:
#         f.write(f'{time_current} end action{n}\n')
#
# def action1(n):
#     print('starting action1...')
#     logger(n)
#
# def action2(n):
#     print('starting action2...')
#     logger(n)
#
# def action3(n):
#     print('starting action3...')
#     logger(n)
#
# action1(11)
# action2(22)
# action3(33)

# def print_info(name,age,sex='male'):    #sex='male'默認參數
#
#     print(f'Name:{name}')
#     print(f'Age:{age}')
#     print(f'Sex:{sex}')
#
# print_info('Jerry',28)      #必需參數
# print_info(name='Janny',age=20,sex='female')     #關鍵字參數


# **kwargs(字典)是不定長參數,成組鍵值對的字典的有命名參數
# def print_info(*args,**kwargs,):
#
#     print(kwargs)
#     for i in kwargs:
#         print(f'{i}:{kwargs[i]}')    #kwargs[i]就可以獲取值出來
#
# print_info(job='IT', hobby='girls', height=176,)

# 關於不定長參數的位置:*args放在前面,**kwargs參數放在後面


