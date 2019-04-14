# -*- conding:utf-8 -*-
# @Time    :2019/3/14 21:29
# @Author  :yahs0105
# @FileName:三級菜單IO.py
# @Ide     :PyCharm

# -*- conding:utf-8 -*-
# @Time    :2019/3/10 14:50
# @Author  :yahs0105
# @FileName:三級菜單.py
# @Ide     :PyCharm


# 高大上版

current_layer = menu #實現動態循環
parent_layers = [] #保存所有父級,最后一個元素永遠都是父級

while True:
    for key in current_layer:
        print(key)
    choice = input('>>>:').strip()
    if len(choice) == 0:continue
    if choice in current_layer:
        parent_layers.append(current_layer)
        # 在進入下一層之前,把當前層(也就是下一層級)追加到列表中下一次loop
        # 當用戶選擇b的選擇,就可以直接取列表的最後一個值出來就ok了
        current_layer = current_layer[choice]
    elif choice == 'b':
        if parent_layers:
            current_layer = parent_layers.pop()#取出列表的最後一個值,因為它就是當前層的父級
    else:
        print('無此項')






