# -*- conding:utf-8 -*-
# @Time    :2019/6/2 16:25
# @Author  :yahs0105
# @FileName:re正則表逹式.py
# @Ide     :PyCharm









import re

#1 findall 返回所有滿足匹配條件的結困,放在列表里
str = "24523oiwrpokdsnjviqwuenmjeddysdvio[uqwrnmcoigt"

print(re.findall("j...y",str))

#2 search 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

print(re.search("j...y",str))

#3 match 同search,不过尽在字符串开始处进行匹配
print(re.match("\d+",str))

#4 split 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割

str = "24523oiwr pokdsn jviqwue nmjed dysdvio-=0uqwrn mcoigt"
print(re.split("[ -]",str))

#5
strs = "24523oiwr pokdsn jviqwue nmjed dysdvio-=0uqwrn mcoigt"
print(re.sub("\d","A",strs,4))

#6
strs = "24523oiwr pokdsn jviqwue nmjed dysdvio-=0uqwrn mcoigt"
print(re.subn("\d","A",strs))

#7
strs = "24523oiwr pokdsn jviqwue nmjed dysdvio-=0uqwrn mcoigt"
com = re.compile("\d+")
print(com.findall(str))





