# -*- conding:utf-8 -*-
# @Time    :2019/3/3 12:12
# @Author  :yahs0105
# @FileName:格式化輸出.py
# @Ide     :PyCharm


name = input("Name:")
age = int(input("Age:"))#將age轉成數字類型方可計算
job = input("Job:")
salary = input("salary:")

# # if salary.isdigit():#指salary長的像不像數字,比如200d,'200'
# #     salary = int(salary)
# # else:
# #     #print()
# #     exit("只能輸入數字")#直接退出程序
#
#
# #str.format
# msg ="""
# --------- info of {0} ---------
# Name   :{0}
# Age    :{1}
# Job    :{2}
# Salary :{3}
# You are retired in {4} years.
# --------- end ---------
# """.format(name,age,job,salary,65-age)
# print(msg)

# for x in range(1, 11):
#     print('{0:5d} {1:5d}'.format(x, x*x))#5d是指,字符串格式化%d格式化為整数

# # f-string
# 在引號外加f帶入參數{}裡的變數
# print(f'''
# --------- info of {name} ---------
# Name   :{name}
# Age    :{age}
# Job    :{job}
# Salary :{salary}
# You are retired in {65-age} years.
# --------- end ---------
# ''')


