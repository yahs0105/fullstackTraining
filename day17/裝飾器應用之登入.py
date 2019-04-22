# -*- conding:utf-8 -*-
# @Time    :2019/4/14 21:10
# @Author  :yahs0105
# @FileName:裝飾器應用之登入.py
# @Ide     :PyCharm

content = input('＞＞＞').strip()


num = 0
for i in content:
    if i.isalpha():
        content = content.split(i,' ')
    num += int(i)
print(num)










