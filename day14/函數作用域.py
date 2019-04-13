# -*- conding:utf-8 -*-
# @Time    :2019/4/13 23:41
# @Author  :yahs0105
# @FileName:函數作用域.py
# @Ide     :PyCharm

# if True:
#     x = 3
# print(x)

# def f():
#     a = 10
#     return a
#
# print(f())


# x = int(2.9)    #int built-in
#
# g_count = 0     #global
#
# def outer():
#     o_count = 1 #enclosing
#     i_count = 8 #優先取local,如果找不到再取enclosing裡的
#     def inner():
#         i_count = 2 #local
#         print(o_count)
#
#     # print(i_count)找不到
#     inner()
#
# outer()


# count = 10
#
# def outer():
#     global count  #如果先宣告為全局以下count=5和count+=1就可以修改
#     print(count)
#     count=5       #print(count)時己調用全局的count,系統將此判定為全局的count,但在局部時不可修改全局變量
#                   #如果把他放在print之前就會被當成局部變量才可以使用
#     count+=1      #也為錯誤因count+=1等於count=count+1也是先調用為全局變量,全局變量不可在局部時修改
#
# outer()


def outer():
    count = 10
    def inner():
        nonlocal count  #ninlocal用於修改enclosing變量用,和global用法相同但作用域不同
        count = 20
        print(count)
    inner()
    print(count)


