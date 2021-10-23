'''
用于手动复制教师名录后的整理
'''

import json, re

# 日期正则式
date = re.compile(r'\d\d\d\d-\d\d-\d\d')

# 1.txt 存放手动复制的教师名录
with open('1.txt', encoding="utf-8") as f:
    contents = f.read()

# 使用 split 方法初步生成名单 list
names = contents.split()

# 二字名中间往往有空格，导致被分为两个 item
for i in range(len(names)):
    # 如果某 item 是单字，说明是二字名的一部分
    if (len(names[i]) == 1 and len(names[i+1]) == 1):
        names[i] += names[i+1]      # 跟后一个 item 合并
        names[i+1] = ''             # 被合并后应该把自身清零，避免影响到下一个名字

for i in range(len(names)):
    # 清除 list 中的空字符串
    if ('' in names):
        names.remove('')

# 删除 list 中的日期
# 因为在循环中会删除 item，所以应该先复制一个 list
names2 = names[:]
for name in names2:
    mo = date.search(name)
    if mo:
        names.remove(mo.group())

# 保存 name list，注意调整 filename
filename = 'change_me.json'
with open(filename, 'w', encoding='utf-8') as f:
    # ensure_ascii=False 参数可避免中文被转为 ascii 码
    json.dump(names, f, ensure_ascii=False)