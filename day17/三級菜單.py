# -*- conding:utf-8 -*-
# @Time    :2019/5/5 16:23
# @Author  :yahs0105
# @FileName:三級菜單.py
# @Ide     :PyCharm


db ={}
path =[]

while True:
    temp = db
    for item in path:
        temp = temp[item]
    print('當前節點的所有子節點:',list(temp.keys()),'\n')

    choice = input('1:添加節點; 2:查看節點;(Q退出/B返回上層)\n>>>')
    if choice == '1':
        k = input('請輸入要添加的子節點名稱:')
        if k in temp:
            print('節點己存在')
        else:
            temp[k] = {}
    elif choice == '2':
        k = input('請輸入要查看的子節點名稱:')
        if k in temp:
            path.append(k)
    elif choice.lower() == 'b':
        if path:
            path.pop()
    elif choice.lower() == 'q':
        break
    else:
        print('輸入不合法')


