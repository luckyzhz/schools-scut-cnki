#! python3
# school_abbrs_and_names.py - 下载学院名及对应的字母缩写

import json
from time import sleep
from selenium import webdriver

url = 'https://www.scut.edu.cn/new/8996/list.htm'
browser = webdriver.Firefox()
browser.get(url)
sleep(10)

school_abbrs_and_names = {}
css_selectors = ['div.left:nth-child(6) a:nth-child(1)', 'div.right:nth-child(7) a:nth-child(1)']

# 获取学院链接
for css_selector in css_selectors:
    schools = browser.find_elements_by_css_selector(css_selector)
    for school in schools:
        school_name = school.text   # 学院名
        school_abbr = school.get_attribute('href').split('/')[3].lower()    # 学院字母缩写
        school_abbrs_and_names[school_abbr] = school_name


# 把 school_abbrs_and_names 存储到文件
filename = 'school_abbrs_and_names.json'
with open(filename, 'w', encoding="utf-8") as f:
    # 设置 ensure_ascii=False，避免中文被保存为 ascii 码
    json.dump(school_abbrs_and_names, f, ensure_ascii=False)
