# -*- conding:utf-8 -*-
# @Time    :2019/3/3 16:54
# @Author  :yahs0105
# @FileName:login2.py
# @Ide     :PyCharm

_user = "Jerry"
_passwd = "12345"
counter = 0

while counter < 3:  #counter為計算次數,當while後面成立(True),才會執行它下面的代碼
    username = input("Usename:")
    password = input("Password:")

    if username == _user and password == _passwd:
        print(f"Welcome {_user} login....")
        break #跳出,中斷 break for過後,就不會執行最後面的else語句

    else:
        print("Invealid username or password !!!")

    counter += 1
    if counter == 3:
        keep_going_choice = input("再來一次嗎?[y/n]")
        if keep_going_choice == "y":
            countre = 0
else:
    print("失敗3次了,滾 !!!")