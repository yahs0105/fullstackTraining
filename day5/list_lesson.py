# -*- conding:utf-8 -*-
# @Time    :2019/3/3 21:42
# @Author  :yahs0105
# @FileName:list_lesson.py
# @Ide     :PyCharm

# a = ['jerry','pete','wei','terry','joe']

#增刪改查

# #增
# #查詢-切片
# print(a[1:])#從第2個到最後一個( 空值 為取最後一個位置)
# print(a[1:-1])#從第2個到 倒數第2個
# print(a[1:-1:1])#第三位置 為從左到右的 步長(默認值為1可不輸入)
# print(a[1::2])#從左到右隔1個去取
# print(a[3::-2])#從第4個索引往右隔1個取
# print(a[-2::-1])#從第4個索引往右每個取

# print(a.count('yung'))
# print('yung' in a)

# #添加 append insert
# a.append('fu')#默認插到最後一個位置
# print(a)
# a.insert(1,'fu')#將數據插入到任意一個位置
# print(a)

# # 修改
# a[1] = 'sabbat'
# print(a)
# a[1:3] = ['a','b']
# print(a)

# 刪除 remove pop del
# a.remove('jerry')
# print(a)
# a.pop(1)
# b = a.pop(1)
# print(a)
# print(b)
# del a[0] #del可以刪除所有東西包含直接刪除list
# print(a)

# count 統計芋個元素在列表中出現的次數
# t =['to','be','or','not','to','be'].count('to')
# print(t)

# extend 可在列表的未尾一次性追加另一個 序列中的多個值(列表)
# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
# print(a)
# print(b)

# index 取得列表中某個值的位置(如多個相同的值取第1個)
# a = ['jerry','pete','wei','terry','joe','wei']

# # 取第1個wei
# first_wei_index = a.index("wei")
# print('first_wei_index',first_wei_index)
#
# #切片取小列表
# little_list = a[first_wei_index+1:]
#
# #取第二個wei在小列表裡的位置
# second_wei_index = little_list.index("wei")
# print('second_little_list',second_wei_index)
#
# #通過first和second位置計算,second在 大列表 里的位置
# second_wei_index_in_big_list = first_wei_index +second_wei_index+1
#
# print('second_wei_index_in_big_list',second_wei_index_in_big_list)
# print('second wei:',a[second_wei_index_in_big_list])

# reverse 對原列表進行倒排序

a = ['jerry','pete','wei','terry','joe','wei']
a.reverse()
print(a)

# sort 用于原位置對列表依ASCII碼進行排序
x = [3,25,127,30,2,8,0]
x.sort() #序
print(x)
