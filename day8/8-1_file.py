# -*- conding:utf-8 -*-
# @Time    :2019/3/10 20:13
# @Author  :yahs0105
# @FileName:8-1_file.py
# @Ide     :PyCharm

# li = [1,2,3]
# li.append(2) #li本身都是一個對象(列表對象),.append(2)是調用的方法
# '123'.capitalize() #'123'本身都是一個對象(字符串對象),.capitalize()是調用的方法

# #打開
# f = open('小重山2','w',encoding='utf8')
#
# #操作
# # data =f.read()
# # print(data)
# data =f.write('hello\n')
# data =f.write('Jerry')
#
# #關閉
# f.close()


# f = open('小重山','r',encoding='utf8')
#
# #操作
# # data =f.read()
# # print(data)
#
# # data =f.write('hello\n')
# # data =f.write('Jerry')
#
# #關閉
# f.close()


# f = open('小重山','r',encoding='utf8')
# # print(f.readline())
# # print(f.readline())
#
#
# count = 0
# for i in f.readlines():
#     count += 1
#
#     if count == 6:
#         i = ''.join([i.strip(),'Hello Word']) #取代萬惡的+
#
#     print(i.strip())
#
# f.close()


# 先取出文件設定一變量去做修改
# f = open('小重山','r',encoding='utf8')
# # print(f.readline())
# # print(f.readline())
# data = f.readlines()
# f.close()
#
# count = 0
# for i in data:
#     count += 1
#
#     if count == 6:
#         i = ''.join([i.strip(),'Hello Word']) #取代萬惡的+
#
#     print(i.strip())


# f = open('小重山','r',encoding='utf8')
#
# for i,v in enumerate(f,1): #這是for內部將f對象做成一個迭代器,用一行取一行
#     if i == 6:
#         v = ''.join([v.strip(),'Hello Word']) #取代萬惡的+
#
#     print(v.strip())
#
# f.close()

# import sys,time
# for i in range(30):
#     sys.stdout.write('*')
#     sys.stdout.flush()  #直接週用flush的方法
#     time.sleep(0.1)

# import sys, time
# for i in range(30):
#     print('*',end='',flush=True)  #使用print裡的flush的參數
#     time.sleep(0.1)

