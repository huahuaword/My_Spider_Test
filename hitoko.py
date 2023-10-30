# -*- coding: utf-8 -*-
"""
@author 比克
@date 2023年10月30日 20:28:31
@packageName 
@className 随机一言
@version 1.0.0
@describe TODO
"""
import requests

def hitokoto():
    try:
        url = 'https://v1.hitokoto.cn/'
        headers = {}
        response = requests.get(url, headers=headers)
        result = response.json()
        return result['hitokoto']
    except Exception as error:
        print(error)

# 示例用法
quote = hitokoto()
print(quote)
