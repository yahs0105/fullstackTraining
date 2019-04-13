# -*- conding:utf-8 -*-
# @Time    :2019/4/8 23:32
# @Author  :yahs0105
# @FileName:集合set.py
# @Ide     :PyCharm

#集合的創建

# a = [1,2,3]
# b = list([4,5,6])
# b = tuple([4,5,6])
# print(a)
# print(b)

# s = set('Jerry Yeh')
# s1 = ['yang','ee','yang']
# s2 = set(s1)
#
# print(s) #{'y', 'r', 'e', 'Y', ' ', 'J', 'h'}
# print(set(s1)) #{'ee', 'yang'} #set有去重功能
# print(s2,type(s2))
#
# s = list(s2)
# print(s,type(s))

a = set([1,2,3,4,5])
b = set([4,5,6,7,8])

# #交集(&)  intersection()
# print(a.intersection(b))
# print(a & b)
#
# #並集(|)  union()
# print(a.union(b))
# print(a | b)
#
# #差集(-)
# print(a.difference(b))
# print(b.difference(a))
# print(a - b)
#
# #反向交集(^)
# print(a.symmetric_difference(b))
# print(a ^ b)
#
# #父集 或叫 超集(>)
# print(a.issuperset(b))
# print(a > b)
#
# #子集(<)
# print(a.issubset(b))
# print(a < b)



