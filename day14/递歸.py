# -*- conding:utf-8 -*-
# @Time    :2019/4/14 12:11
# @Author  :yahs0105
# @FileName:递歸.py
# @Ide     :PyCharm


# def f(n):
#     if n==1:
#         return 1
#
#     return n*f(n-1)
#
# print(f(5))

# 關於递歸的特點:
#   1.調用自身函數
#   2.必需有一個結束條件
# 但凡是递歸可以寫的程序,循環都可以解決
# 递歸的效率在很多時後會很低,不推建使用


#菲波那契數列:0 1 1 2 3 5 8 13 21

#以for返圈表示
# def fibo(n):
#     before = 0
#     after = 1
#     for i in range(n-1):
#         ret = before+after
#         before=after
#         after=ret
#     return ret
#
# print(fibo(8))

#以递歸表示

# def fibo(n):
#
#     if n <= 2:
#         return n
#     return fibo(n-1) + fibo(n-2)

