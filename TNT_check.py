"""

@比克出品 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
qq裙:638680122
TNT_Check_V0.1   签到
添加环境变量：
BASE_URL：目标签到网站
SCKEY：pushplus的token
EMAIL：账号
PASSWORD：密码
cron： 0 0 7 * * ?

"""
import requests
import json
import os
requests.packages.urllib3.disable_warnings()
SCKEY = os.environ['SCKEY']
def checkin(email=os.environ['EMAIL'], password=os.environ['PASSWORD'],
            base_url=os.environ['BASE_URL']):
    email = email.split('@')
    email = email[0] + '%40' + email[1]
    session = requests.session()
    session.get(base_url, verify=False)
    login_url = base_url + '/auth/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/56.0.2924.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    post_data = 'email=' + email + '&passwd=' + password + '&code='
    post_data = post_data.encode()
    response = session.post(login_url, post_data, headers=headers, verify=False)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/56.0.2924.87 Safari/537.36',
        'Referer': base_url + '/user'
    }
    response = session.post(base_url + '/user/checkin', headers=headers,
                            verify=False)
    response = json.loads(response.text)
    print(response['msg'])
    return response['msg']


if SCKEY != '':
    sendurl = 'http://www.pushplus.plus/send?token=' + SCKEY + '&title=机场签到&content=' + checkin()
    r = requests.get(url=sendurl)
