# -*- coding: utf-8 -*-
"""
@author 比克
@date 2024年09月28日 10:34:53
@packageName 
@className baidunews
@version 1.0.0
@describe TODO
"""

import requests
from lxml import html
import json
import urllib.parse

url = "https://www.baidu.com"  # 替换为你需要的URL
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    tree = html.fromstring(response.content)
    # 获取XPath对应的内容
    content = tree.xpath('//*[@id="hotsearch_data"]/text()')

    if content:
        # 假设 content 中是一个 JSON 字符串
        json_data = json.loads(content[0])  # 获取第一个元素并解析为 JSON

        # 提取 card_title 和 linkurl，并排序输出
        for index, item in enumerate(json_data["hotsearch"], start=1):
            card_title = item["card_title"]
            linkurl = urllib.parse.unquote(item["linkurl"])  # 解码 URL
            SCKEY = "你的pushplustoken"
            if SCKEY:
                print(f"{index}. {card_title}, Link: {linkurl}")
                sendurl = f'http://www.pushplus.plus/send?token={SCKEY}&title=机场签到&content={f"{index}. {card_title}, Link: {linkurl}"}'
                r = requests.get(url=sendurl)
                # print("推送结果:", r.text)
            else:
                print("没有设置 SCKEY，无法推送签到结果")
            # print(f"{index}. {card_title}, Link: {linkurl}")
    else:
        print("没有获取到内容")
else:
    print("请求失败，状态码:", response.status_code)



