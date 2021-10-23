#! python3
# materials.py - 下载【材料科学与工程学院】教师名录

import json
from time import sleep
from selenium import webdriver

url = 'http://www2.scut.edu.cn/materials/szdw/list.htm'
browser = webdriver.Firefox()
browser.get(url)
sleep(10)

names = []

# 获取所有系
departments = browser.find_elements_by_css_selector('.teacher-list-item')

# 依次展开每个系
for i in range(len(departments)):
    # browser.execute_script("arguments[0].setAttribute('class', 'selected')", departments[i])
    departments[i].click()
    teachers = browser.find_elements_by_css_selector(f'.teacher-list-item:nth-child({i+1}) a')
    for teacher in teachers:
        names.append(teacher.text)

# 把 names 存储到文件
filename = 'materials.json'
with open(filename, 'w', encoding="utf-8") as f:
    # 设置 ensure_ascii=False，避免中文被保存为 ascii 码
    json.dump(names, f, ensure_ascii=False)