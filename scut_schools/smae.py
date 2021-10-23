#! python3
# smae.py - 下载【机械与汽车工程学院】教师名录

import json
from selenium import webdriver

url = 'http://www2.scut.edu.cn/smae/20493/list.htm'
browser = webdriver.Firefox()
browser.get(url)

# 点击【按系所查找】按钮
departments_button = browser.find_element_by_css_selector('#B102')
departments_button.click()

# 获取所有系所，以便后面点击展开
xisuos = browser.find_elements_by_css_selector('#tb_B102 > div')

# 存储所有老师的 list
all_teachers = []

# 遍历所有系所
for i in range(len(xisuos)):
    browser.execute_script("arguments[0].setAttribute('class','on')", xisuos[i])    # 展开系所

    css_selector = f'#xisuo_{i} .xx_teacher_name'   # 选取展开系所的老师
    teachers = browser.find_elements_by_css_selector(css_selector)
    
    for teacher in teachers:
        # 存储老师名字
        all_teachers.append(teacher.text)

# 把 all_teachers 存储到文件
filename = 'smae.json'
with open(filename, 'w', encoding="utf-8") as f:
    # 设置 ensure_ascii=False，避免中文被保存为 ascii 码
    json.dump(all_teachers, f, ensure_ascii=False)