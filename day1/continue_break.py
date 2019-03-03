# -*- conding:utf-8 -*-
# @Time    :2019/3/3 17:20
# @Author  :yahs0105
# @FileName:continue_break.py
# @Ide     :PyCharm

exit_flag = False
for i in range(10):
    if i < 5:
        continue
    print(i)
    for j in range(10):
        print("laver2":j)
        if j == 6:
            exit_flag = True#
            break
    if exit_flag:
        bresk