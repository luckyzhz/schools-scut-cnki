#! python3
# wusie.py - 下载【吴贤铭智能工程学院】教师名录

import json
from time import sleep
from selenium import webdriver

url = 'http://www2.scut.edu.cn/wusie/szll/list.htm'
browser = webdriver.Firefox()
browser.get(url)
sleep(10)

names = []

teachers = browser.find_elements_by_css_selector('.shi-ultt a')
for teacher in teachers:
    # 使用 str.replace() 去除姓名中的空格
    names.append(teacher.text.replace(' ', ''))

# 把 names 存储到文件
filename = 'wusie.json'
with open(filename, 'w', encoding="utf-8") as f:
    # 设置 ensure_ascii=False，避免中文被保存为 ascii 码
    json.dump(names, f, ensure_ascii=False)