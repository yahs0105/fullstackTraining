# -*- conding:utf-8 -*-
# @Time    :2019/5/12 20:26
# @Author  :yahs0105
# @FileName:global_and_local.py
# @Ide     :PyCharm


name = '杠娘'
def weihou():
    name ='陳卓'
    def weiweihou():
        global name
        name = '冷靜'
    weiweihou()
    print(name)







