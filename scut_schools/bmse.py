#! python3
# bmse.py - 下载【生物医学科学与工程学院】教师名录

import json
from time import sleep
from selenium import webdriver

url = 'http://www2.scut.edu.cn/bmse/szdw/list1.htm'
browser = webdriver.Firefox()
browser.get(url)
sleep(10)

names = []
n = browser.find_element_by_css_selector('.all_pages').text
n = int(n)

for i in range(n):
    teachers = browser.find_elements_by_css_selector('.info-one .name')
    for teacher in teachers:
        # 使用 str.replace() 去除姓名中的空格
        names.append(teacher.text.replace(' ', ''))
    
    next_page = browser.find_element_by_css_selector('.next')
    next_page.click()
    sleep(10)

# 把 names 存储到文件
filename = 'bmse.json'
with open(filename, 'w', encoding="utf-8") as f:
    # 设置 ensure_ascii=False，避免中文被保存为 ascii 码
    json.dump(names, f, ensure_ascii=False)