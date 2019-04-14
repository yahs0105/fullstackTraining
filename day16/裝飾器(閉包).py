# -*- conding:utf-8 -*-
# @Time    :2019/4/14 15:46
# @Author  :yahs0105
# @FileName:裝飾器(閉包).py
# @Ide     :PyCharm

# 1
# def outer():
#     x=10
#     def inner():    # 滿足條件1: inner就是內部函數
#         print(x)    # 滿足條件2: X就是外部環境的變量
#
#     return inner    # 結論: 內部函數inner就是一個閉包

# 2
# def outer(x):
#     def inner():
#         print(x)
#
#     return inner
# # 調用inner()
# outer(8)()
#
# f=outer(5)
# f()

# inner() # 局部變量,全局無法調用














