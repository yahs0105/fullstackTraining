# -*- conding:utf-8 -*-
# @Time    :2019/3/3 12:12
# @Author  :yahs0105
# @FileName:格式化輸出.py
# @Ide     :PyCharm


name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("salary:")

# if salary.isdigit():#指salary長的像不像數字,比如200d,'200'
#     salary = int(salary)
# else:
#     #print()
#     exit("只能輸入數字")#直接退出程序

msg ="""
--------- info of {} ---------
Name   :{}
Age    :{}
Job    :{}
Salary :{}
You are retired in {} years.
--------- end ---------
""".format(name,name,age,job,salary,65-age)
print(msg)