#! python3
# cnki.py - 下载知网华工论文作者
# 经测试，用德国 ip 可爬到约 2000 条数据。中间出现过一次字符验证码，手动输入解决了

from time import sleep
from random import random, randint
import json
from selenium import webdriver

url = 'https://cnki.net/'
browser = webdriver.Firefox()
browser.get(url)

# 设置搜索选项为【作者单位】
sort_select = browser.find_element_by_css_selector("#DBFieldBox")
sort_select.click() # 展开搜索选项下拉列表
sort = browser.find_element_by_css_selector('#DBFieldList > ul:nth-child(1) > li:nth-child(9) > a:nth-child(1)')
sort.click()    # 选择【作者单位】

# 搜索华南理工
searchText = '华南理工'
searchBox = browser.find_element_by_css_selector('#txt_SearchText')
searchBox.send_keys(searchText)
searchButton = browser.find_element_by_css_selector('.search-btn')
searchButton.click()
sleep(10)

# 设置每页显示 50 条记录
show_number = browser.find_element_by_css_selector('#perPageDiv')
show_number.click()
show_50 = browser.find_element_by_css_selector('ul.sort-list > li:nth-child(3) > a:nth-child(1)')
show_50.click()
sleep(10)

# 存储文章题目和作者。数据结构[{'title': 'xxx', 'authors': [a1, a2, a3]}]
articles = []

# 获取前 300 页的记录
for i in range(300):
    titles = browser.find_elements_by_css_selector('.fz14') # 获取所有文章标题
    all_authors = browser.find_elements_by_css_selector('.author')  # 获取所有作者

    for j in range(len(titles)):
        # 构造每篇文章的信息
        article = {}
        article['title'] = titles[j].text
        article['authors'] = all_authors[j].text.split(';')
        # 添加到文章列表
        articles.append(article)
    
    # 每爬完一页，及时存储
    filename = f'articles_{i+1}.json'
    with open(filename, 'w', encoding="utf-8") as f:
        # 设置 ensure_ascii=False，避免中文被保存为 ascii 码
        json.dump(articles, f, ensure_ascii=False)

    # 下一页
    next_page = browser.find_element_by_css_selector('#PageNext')
    next_page.click()
    sleep(10+10*random())
    browser.execute_script("window.scrollBy(0, arguments[0])", randint(150, 600))    # 随机滚动
    sleep(10+10*random())
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")    # 滚动到页面底部
    sleep(10+10*random())

