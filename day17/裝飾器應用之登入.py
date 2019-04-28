# -*- conding:utf-8 -*-
# @Time    :2019/4/14 21:10
# @Author  :yahs0105
# @FileName:裝飾器應用之登入.py
# @Ide     :PyCharm



i = 3
lis = []
while i > 0:
    username = input('請輸入用戶名:')
    passsword = input('請輸入密碼:')
    with open('info', 'r+', encoding='utf-8')as f:
        for line in f:
            lis.append(line)
    if username == lis[0].strip() and passsword == lis[1].strip():
        print(f'~~歡迎{username}您的登入~~')
        break
    elif username!=lis[0]:
        choice = input('無此使用者帳戶'
                       '新註冊請按R:')
        if choice =='R' or choice =='r':
            uname = input('請輸入新用戶名:')
            pword = input('請輸入新密碼:')
            lis = [uname,pword]
            with open('info', 'r+', encoding='utf-8')as f:
                f.read()
                f.write(f'{lis}\n')
        print('恭喜註冊成功,請重新登入')
    else:print(f'查無帳號,己輸入{i-1}次')

    i-=1


# with open('小護士','r+',encoding='utf-8') as f,open('小護士.bak','w+',encoding='utf-8') as f2:
#     for line in f:
#         if '中國' in line:
#             line = line.replace('中國','台灣')
#         f2.write(line)
# import os
# os.remove('小護士')
# os.rename('小護士.bak','小護士')




