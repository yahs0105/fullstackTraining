# -*- conding:utf-8 -*-
# @Time    :2019/3/9 17:04
# @Author  :yahs0105
# @FileName:dict.py
# @Ide     :PyCharm


# dic1 = {'name':'Jerry','age':'37','sex':'male','hobby':'make love'}
# dic2 = {'1':'22','dd':'37'}
# dic3 = {'1':'22','dd':'37','42':23}
# print(dic1)
# print(dic1['name'])
#
#
# dic1.setdefault('gg',18)
#
# print(dic1.keys())
# print(dic1.values())
# print(dic1.items())
#
# dic1.update(dic2)
#
# dic1.clear()
# dic1.pop('name')
# ret = dic1.pop('name')
# print(ret)
#
# a = dic3.popitem()
# print(a,dic3)

# dic4 = dict.fromkeys(['host1','host2','host3'],'test')
#
# print(dic4)#{'host1': 'test', 'host2': 'test', 'host3': 'test'}

# dic4 = dict.fromkeys(['host1','host2','host3'],['test1','test2'])
# dic4['host2'][1]='aaa'
#
# print(sorted(dic4))

# dic5 = {'name':'Jerry','age':'37','sex':'male','hobby':'make love'}
#
# 效率高
# for i in dic5:
#     print(i,dic5[i])
# 效率低
# for i,v in dic5.items():
#     print(i,v)

