# -*- conding:utf-8 -*-
# @Time    :2019/4/8 20:49
# @Author  :yahs0105
# @FileName:深淺拷貝.py
# @Ide     :PyCharm



# s = [l,'aaa','bbb','ccc']
#
# s1 = [l,'aaa','bbb','ccc']
# s1[0] = 2
# print(s)
# print(s1)

# 淺拷貝
# s = [l,'aaa','bbb','ccc']
# s2 = s.copy()
# print(s2)
#
# s2[0] = 3
# print(s)
# print(s2)

# s = [[1,2],'aaa','bbb','ccc']
# s3 = s.copy()
# print(s3)
# # s3[1] = 'JerryYeh'
# # print(s3)
# # print(s)
# s3[0][1] ='a'
# print('s3',s3)
# print('s',s)

# 深拷貝

import copy
husband = ["Jerry",123,[10000,8000]]

wife = husband.copy()
# wife = copy.copy(husband) #shallow copy
wife[0] = "KiKi"
wife[1] = 345

jing = copy.deepcopy(husband)

jing[0] = "Jing"
jing[1] = 666

jing[2][1] -=1000

husband[2][1] -=3000

print(wife)
print(husband)
print(jing)
