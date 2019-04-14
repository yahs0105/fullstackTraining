# -*- conding:utf-8 -*-
# @Time    :2019/3/9 16:42
# @Author  :yahs0105
# @FileName:購物車程序.py
# @Ide     :PyCharm


# 物品清單
item_list = [('IphoneXs Max',52000),
             ('MacBook',32000),
             ('coffe',250),
             ('賈伯斯傳-Steve Jobs',600),
             ('Gogoro',80000),
             ('老婆的生日禮物',10000),
             ]

saving = input('請輸入您的所持金額:')
shopping_car = []
if saving.isdigit():#如果輸入是數字時執行
    saving = int(saving)#輸為數字時轉為int
    while True:
        # 打印商品内容
        for i,v in enumerate(item_list,1):
            print(i,'>>>',v)

        # 引导用户选择商品
        choice = input('''
選擇購買商品編號:
或 退出:q''')

        # 验证输入是否合法
        if choice.isdigit():#如果輸入是數字時執行
            choice = int(choice)#輸為數字時轉為int
            if choice >0 and choice <= len(item_list):#強制輸入的數字於'列表'的長度不超過,len(item_list)指它的總長度

                # 将用户选择商品通过choice取出来
                i_item = item_list[choice-1]#因索引和實際列表位置差異，取出於列表裡的商品元組

                # 如果钱够，用本金saving减去该商品价格，并将该商品加入购物车
                if i_item[1] < saving:#所持金額要大於商品的金額，i_item是己從item_list中取出的元組，i_item[1]指元組的第2位置中的參數
                    saving -= i_item[1]

                    shopping_car.append(i_item)

                else:
                    print(f'餘額不足,您金額剩{saving}'.center(50,'-'))
            else:
                print('此商品編號不存在'.center(50,'-'))

        elif choice == 'q':
            print('您己購買商品如下'.center(50,'-'))
            for i in shopping_car:
                print(i)
            print(f'您的金額剩{saving}元'.center(50,'-'))
            break#為了結束whileh循環，如後面還有程序依然可執行
        else:
            print('輸入錯誤請重新輸入!'.center(50,'-'))