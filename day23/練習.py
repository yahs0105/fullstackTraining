# -*- conding:utf-8 -*-
# @Time    :2019/6/3 23:21
# @Author  :yahs0105
# @FileName:練習.py
# @Ide     :PyCharm

import re

s = "1-2 * ((60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"

str = s.replace(" ","")
print(str)


a0 = re.search("\([^()]+\)",str)

a1 = a0.group()
a2 = re.findall("[^()]+\w+",a1)





