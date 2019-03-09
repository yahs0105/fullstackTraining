# -*- conding:utf-8 -*-
# @Time    :2019/3/3 16:07
# @Author  :yahs0105
# @FileName:Login.py
# @Ide     :PyCharm

# for i in range(1,101):
#     if i % 2 == 1:
#         print("loop: ",i)
#
# for i in range(1,101,2):#2=步長
#     print("loop: ", i)

# for i in range(100):
#     if i < 50 or i>70:
#         print(i)


# _user = "Jerry"
# _passwd = "12345"
#
# passed_authentication = False #flag=標志位,立旗預設
#
# for count in range(3):
#     username = input("Usename:")
#     password = input("Password:")
#
#     if username == _user and password == _passwd:
#         print(f"Welcome {_user} login....")
#         passed_authentication = True
#         break #跳出,中斷
#     else:
#         print("Invealid username or password !!!")
# if not passed_authentication:#只有在False的情況下,條件成立
#     print("失敗3次")


# _user = "Jerry"
# _passwd = "12345"
#
# for count in range(3):
#     username = input("Usename:")
#     password = input("Password:")
#
#     if username == _user and password == _passwd:
#         print(f"Welcome {_user} login....")
#         passed_authentication = True
#         break #跳出,中斷 break for過後,就不會執行最後面的else語句
#     else:
#         print("Invealid username or password !!!")
# else:#只要上面for循環正常執完畢,中間沒被打斷,就會執行這段else語句
#     print("失敗3次")
