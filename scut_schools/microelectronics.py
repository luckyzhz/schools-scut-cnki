#! python3
# microelectronics.py - 下载【微电子学院】教师名录

import json
from time import sleep
from selenium import webdriver

url = 'http://www2.scut.edu.cn/microelectronics/bd/list.htm'
browser = webdriver.Firefox()
browser.get(url)
sleep(10)

names = []

# 获取侧边栏
titles = browser.find_elements_by_css_selector('.ul-bg a')
n = len(titles)

# 依次处理侧边栏的每个链接
for i in range(1, n-1):
    titles = browser.find_elements_by_css_selector('.ul-bg a')
    titles[i].click()
    sleep(10)

    teachers = browser.find_elements_by_css_selector('.name')
    for teacher in teachers:
        # 使用 str.replace() 去除姓名中的空格
        # 只取中文名字，舍弃拼音
        name = teacher.text.split()[0]
        names.append(name)

# 把 names 存储到文件
filename = 'microelectronics.json'
with open(filename, 'w', encoding="utf-8") as f:
    # 设置 ensure_ascii=False，避免中文被保存为 ascii 码
    json.dump(names, f, ensure_ascii=False)