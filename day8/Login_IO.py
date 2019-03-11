# -*- conding:utf-8 -*-
# @Time    :2019/3/11 23:40
# @Author  :yahs0105
# @FileName:Login_IO.py
# @Ide     :PyCharm


data = open('login','r+',encoding='utf8')

for i in range(3):
    username = input("Usename:")
    password = input("Password:")
    if username in data and password in data:
        print(f"Welcome {username} login....")
    elif username in data or password in data:
        print("帳號或密碼錯誤請重新輸入~")
    else:
        print("無此帳號!!!")

else:#只要上面for循環正常執完畢,中間沒被打斷,就會執行這段else語句
    print("失敗3次")
