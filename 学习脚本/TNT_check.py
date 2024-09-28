"""
@比克出品 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
qq裙:638680122
TNT_Check_V0.2   签到
添加环境变量：
BASE_URL：目标签到网站
SCKEY：pushplus的token
EMAIL：账号
PASSWORD：密码
cron： 0 0 7 * * ?
"""
import requests
import json
# import os  非必选项

def login_and_checkin(base_url, email, password):
    # 创建一个Session对象来保持会话
    session = requests.Session()

    # 登录URL和请求头
    login_url = f"{base_url}/auth/login"
    login_headers = {
        'Host': base_url.split('//')[-1],
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'sec-ch-ua-platform': '"Windows"',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': base_url,
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f"{base_url}/auth/login",
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'priority': 'u=1, i'
    }

    login_data = {
        "email": email,
        "passwd": password,
        "code": ""
    }

    # 进行登录请求
    login_response = session.post(login_url, headers=login_headers, data=login_data)

    # 打印登录的响应状态码及Cookies信息
    # print("登录响应状态码:", login_response.status_code)
    # print("登录响应Cookies:", session.cookies.get_dict())

    # 检查登录是否成功
    if login_response.status_code == 200:
        print("登录成功")

        # 签到URL和请求头
        checkin_url = f"{base_url}/user/checkin"
        # 发送签到请求
        checkin_response = session.post(checkin_url, headers=login_headers)

        # 打印签到的响应状态码
        # print("签到响应状态码:", checkin_response.status_code)

        # 将Unicode编码内容转换为正常文本
        decoded_text = checkin_response.text.encode('utf-8').decode('unicode_escape')

        try:
            # 解析JSON并提取msg的值
            json_data = json.loads(decoded_text)
            msg = json_data["msg"]
            print("签到信息:", msg)
            return msg

        except json.JSONDecodeError:
            print("JSON解析失败，返回原始内容:")
            print(decoded_text)
            return None

    else:
        print("登录失败")
        print("登录响应内容:", login_response.text)
        return None

# 使用示例
# base_url = "网址"
# SCKEY = os.environ['SCKEY']
# base_url = os.environ['base_url']
email = "邮箱"
password = "密码"
login_and_checkin(base_url, email, password)
# if SCKEY != '':
#     sendurl = 'http://www.pushplus.plus/send?token=' + SCKEY + '&title=机场签到&content=' + login_and_checkin(base_url, email, password)
#     r = requests.get(url=sendurl)
