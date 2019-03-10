# -*- conding:utf-8 -*-
# @Time    :2019/3/10 14:50
# @Author  :yahs0105
# @FileName:三級菜單.py
# @Ide     :PyCharm

menu = {
    '北部':{
        '台北市': {
            '中正區':{},
            '大同區':{},
            '中山區':{},
        },
        '新北市': {
            '萬里區':{},
            '金山區':{},
            '板橋區':{},
        },
        '桃園市': {
            '桃園區':{},
            '龜山區':{},
            '中壢區':{},
        },
        '新竹市': {
            '東區':{},
            '北區':{},
            '香山區':{},
        },
    },
    '中部':{
        '台中市': {
            '中區':{},
            '東區':{},
            '南區':{},
            '北區':{},
        },
        '雲林縣': {
            '斗南鎮':{},
            '虎尾鎮':{},
            '土庫鎮':{},
        },
        '彰化縣': {
            '彰化市':{},
            '花園鄉':{},
            '秀水鄉':{},
            '鹿港鎮':{},
        },
        '南投縣': {
            '南投市':{},
            '中寮鄉':{},
            '草屯鎮':{},
            '國姓鄉':{},
        }
    },
    '南部':{
        '台南市': {
            '中西區':{},
            '東區':{},
            '南區':{},
            '北區':{},
        },
        '高雄市': {
            '新興區':{},
            '前金區':{},
            '苓雅區':{},
            '三民區':{},
        },
        '嘉義縣': {
            '番路鄉':{},
            '竹崎鄉':{},
            '梅山鄉':{},
            '阿里山鄉':{},
        },
        '屏東縣': {
            '屏東鄉':{},
            '三地門鄉':{},
            '瑪家鄉':{},
        },
    },
    '東部':{
        '台東縣': {
            '台東市':{},
            '綠島鄉':{},
            '蘭嶼鄉':{},
        },
        '花蓮縣': {
            '花蓮市':{},
            '新城鄉':{},
            '秀林鄉':{},
        },
        '宜蘭縣': {
            '宜蘭市':{},
            '頭城鎮':{},
            '礁溪鄉':{},
        },
    }
       }


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





