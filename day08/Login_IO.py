# -*- conding:utf-8 -*-
# @Time    :2019/3/11 23:40
# @Author  :yahs0105
# @FileName:Login_IO.py
# @Ide     :PyCharm




for i in range(3):
    data = open('login', 'r+', encoding='utf8')
    username = input("Usename:")
    password = input("Password:")
    if username in data.read() and password in data.read():
        print(f"Welcome {username} login....")
        break
    elif username in data.read() or password in data.read():
        print("帳號或密碼錯誤請重新輸入~")
    else:
        choice = input('無此帳號!!!註冊成新帳號請按"r"')
        if choice == 'r' :
            print('註冊新帳號')
            username = input("請輸入新註冊 Usename:")
            password = input("請輸入新註冊 Password:")
            i = f'{username},{password}\n'
            data.write(i)
            data.flush()
    data.close()
else:#只要上面for循環正常執完畢,中間沒被打斷,就會執行這段else語句
    print("失敗3次")
