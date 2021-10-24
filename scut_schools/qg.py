#! python3
# qg.py - 下载【轻工科学与工程学院】教师名录

import json
from time import sleep
from selenium import webdriver

url = 'http://www2.scut.edu.cn/qgkxygc/jsfc/list.htm'
browser = webdriver.Firefox()
browser.get(url)
sleep(10)

names = []

# 获取侧边栏
titles = browser.find_elements_by_css_selector('.wp_subcolumn a')
n = len(titles)

# 依次处理侧边栏的每个链接
for i in range(n):
    titles = browser.find_elements_by_css_selector('.wp_subcolumn a')
    titles[i].click()
    sleep(10)

    teachers = browser.find_elements_by_css_selector('.teacherlist span a')
    for teacher in teachers:
        # 使用 str.replace() 去除姓名中的空格
        names.append(teacher.text.replace(' ', ''))

# 把 names 存储到文件
filename = 'qg.json'
with open(filename, 'w', encoding="utf-8") as f:
    # 设置 ensure_ascii=False，避免中文被保存为 ascii 码
    json.dump(names, f, ensure_ascii=False)