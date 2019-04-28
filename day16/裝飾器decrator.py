# -*- conding:utf-8 -*-
# @Time    :2019/4/14 18:53
# @Author  :yahs0105
# @FileName:裝飾器decrator.py
# @Ide     :PyCharm

import time

#運用閉包函數去包裝成的裝飾器就可在原代碼上增加新功能上去
def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print(f'spend:{end-start}')

    return inner
#裝飾器 用@加上函數名例:@show_time
@show_time  #foo = show_time(foo)
def foo():
    print('foo...')
    time.sleep(0.1)

@show_time  #bar = show_time(bar)
def bar():
    print('bar...')
    time.sleep(0.3)

foo()
bar()


功能函數加參數
def show_time(f):
    def inner(*x,**y):
        start = time.time()
        f(*x,**y)
        end = time.time()
        print(f'spend:{end-start}')

    return inner


@show_time  #foo = show_time(foo)
def add(*a,**b):
    sums=0
    for i in a:
        sums+=i
    print(sums)
    time.sleep(0.5)

add(1,3,23,5,2)


# 裝飾器加參數
def logger(flag=''):
    def show_time(f):
        def inner(*x,**y):
            start = time.time()
            f(*x,**y)
            end = time.time()
            print(f'spend:{end-start}')
            if flag == 'l':
                print('日誌記錄')
        return inner
    return show_time

@logger('l')
def add(*a,**b):
    sums=0
    for i in a:
        sums+=i
    print(sums)
    time.sleep(0.5)

add(1,3,23,5,2)







