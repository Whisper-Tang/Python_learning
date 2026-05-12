# xpath简单语法
# 表达式              描述                        样例
# /                 从根节点开始选择所有节点         /html/body/p
# //                从任意位置选择节点              //p
# @                 选择属性节点                    @class
# .                 从当前节点向下寻找              .
# ..                从当前节点向父节点向下寻找       ..
# [n]               选择第ｎ个元素                  //p[2]
# [last()]          选择最后一个元素                //p[last()]
# [last() - n]      选择倒数第ｎ个元素              //p[last() - 1]
# [@attr]           选择有该属性的元素              @class
# [@attr="value"]   选择属性值为value的元素         @class="active"
# *                 选择所有元素                    *
# @*                选择所有属性                    @*
# @*="value"        选择属性值为value的元素          @class="active"
# text()            选择所有文本节点                 text()
# 爬取op.gg的tier排行榜

from math import e
import lxml
import lxml.html
import requests

import os

file_path = 'Python_learning/opgg_tier.html'


target_url = 'https://op.gg/zh-cn/lol/leaderboards/tier'
if not os.path.exists(file_path):
    response = requests.get(target_url)
    if response.status_code == 200:
        print('请求成功')
    else:
        print('请求失败')
    # print(response.text)
    document = lxml.html.fromstring(response.text)

    with open('Python_learning/opgg_tier.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
        print('文件已保存')
else:
    print('文件已存在')
    document = lxml.html.parse(file_path)

head_list = document.xpath('//main/table/thead/tr/th/text()')
# print(head_list)
# 选择排名列
rank_list = document.xpath(
    '//main/table/tbody/tr/td[1]/text()')
# print(rank_list)
# 召唤师
summor_list = document.xpath('//main/table/tbody/tr/@id')
# print(summor_list)
# 删选出等级且不为空白的元素
# 段位
tier_list = document.xpath(
    '//main/table/tbody/tr/td[3]/div/text()')
# print(tier_list)
# 天梯分
lp_list = document.xpath('//main/table/tbody/tr/td[4]/div/text()')
# print(lp_list)
# 最多使用的英雄
# mostchampion_list = document.xpath(
#     '//main/table/tbody/tr/td[5]/div/a/@data-tooltip-content')
# print(len(mostchampion_list))
# mostchampion_list = [mostchampion_list[i:i+3]
#                      for i in range(0, len(mostchampion_list), 3)]
mostchampion_rows = document.xpath('//main/table/tbody/tr/td[5]/div')
mostchampion_list = []
for row in mostchampion_rows:
    mostchampion_list.append(row.xpath('./a/@data-tooltip-content'))
# print(len(mostchampion_list))
# for i in range(100):
#     print(i+1,mostchampion_list[i])


# 等级
level_list = document.xpath('//main/table/tbody/tr/td[6]/text()')
# print(level_list)
# 胜场数(四个元素一组：场数，胜，场数，负)
wincount_list = document.xpath(
    '//main/table/tbody/tr/td[7]/div/div/div[*]/span/text()')
# print(wincount_list)
wincount_list = [[int(wincount_list[i]), int(wincount_list[i+2])]
                 for i in range(0, len(wincount_list), 4)]
# print(wincount_list)
# print(wincount_list[1][0], wincount_list[1][1])
# print(int(wincount_list[1][0]), int(wincount_list[1][1]))

# 胜率
winrate_list = document.xpath(
    '//main/table/tbody/tr/td[7]/div/span/text()')
# print(winrate_list)


class summor_data:
    # 定义类的属性
    rank = 0
    summor = ''
    tier = ''
    lp = 0
    mostchampion = ['', '', '']
    level = 0
    win = 0
    loss = 0
    winrate = ''

    def __init__(self, rank: int, summor: str, tier: str, lp: int, mostchampion: list, level: int, win: int, loss: int, winrate: str):
        self.rank = rank
        self.summor = summor
        self.tier = tier.capitalize()
        self.lp = lp
        self.mostchampion = mostchampion
        self.level = level
        self.win = win
        self.loss = loss
        self.winrate = winrate

    # def __str__(self):
    #     mostchampion_str = ', '.join(self.mostchampion) if self.mostchampion else '无'
    #     return f'{self.rank} {self.summor}\t{self.tier} {self.lp}\n{mostchampion_str}\n{self.level}\t{self.win}\\{self.loss}\t{self.winrate}\n'
    def __str__(self):
        mostchampion_str = '/'.join(
            self.mostchampion) if self.mostchampion else '无'
        #return f'{self.rank}\t{self.summor}\t{self.tier}\t{self.lp}\t{mostchampion_str}\t{self.level}\t{self.win}\\{self.loss} {self.winrate}\n'
        return f'{self.rank},{self.summor},{self.tier},{self.lp},{mostchampion_str},{self.level},{self.win},{self.loss},{self.winrate}\n'

# print(len(rank_list))
# print(len(summor_list))
# print(len(tier_list))
# print(len(lp_list))
# print(len(mostchampion_list))
# print(len(level_list))
# print(len(wincount_list))
# print(len(winrate_list))
# for i in range(100):
#     print(i+1,mostchampion_list[i])
rank_data_list = []
head_title = ','.join(head_list)
# print(head_title)
with open('/mnt/c/Users/WhisperTang/Desktop/opgg_tier.txt', 'w', encoding='utf-8-sig') as f:
    f.write(head_title + '\n')
    for i in range(len(rank_list)):
        rank_data_list.append(summor_data(
            int(rank_list[i]),          # 排名
            summor_list[i].replace('-', '#'),             # 召唤师
            tier_list[i],             # 段位
            int(lp_list[i].replace(',', '')),           # 天梯分
            mostchampion_list[i],     # 最多使用的英雄
            int(level_list[i].replace(',', '')),       # 等级
            int(wincount_list[i][0]),   # 胜场数
            int(wincount_list[i][1]),   # 负场数
            winrate_list[i]))      # 胜率
        f.write(str(rank_data_list[i]))

# 保存到csv文件
# CSV文件：逗号分隔值文件
# 每个数据项之间用逗号分隔
# 每个数据项之间用换行符分隔

import csv

with open('/mnt/c/Users/WhisperTang/Desktop/opgg_tier.csv', 'w', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(head_list)  # 写入表头
    for data in rank_data_list:
        writer.writerow([data.rank, data.summor, data.tier, data.lp, '/'.join(data.mostchampion), data.level,str(data.win)+'/'+str(data.loss), data.winrate])
# 将csv文件

