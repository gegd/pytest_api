import requests
import re
import os


def login(session):
    """实现登录的功能"""
    url = 'http://49.235.92.12:9000/api/v1/login/'
    params = {
        'username': 'test',
        'password': '123456'
    }
    res = session.post(url=url, json=params)
    print(session.headers)
    print(res.json())

    # 获取登录token

    token = res.json().get('token')
    header = {
        'Authorization': 'Token %s' % token
    }

    session.headers.update(header)
    # 更新之后的header
    print(session.headers)
    return token


def login_xadmin(session):
    url = os.environ['xadmin_host'] + '/xadmin/'
    res = session.get(url)
    # print(res.text)
    token = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", res.text)
    print(token[0])
    body = {
        'csrfmiddlewaretoken': token[0],
        'username': 'admin',
        'password': 'yoyo123456',
        'this_is_the_login_form': 1,
        'next': '/xadmin/'
    }
    result = session.post(url=url, data=body)
    # print(result.text)
    if '主页面 | 后台页面' in result.text:
        print('登录成功')
    else:
        print('登录失败')



if __name__ == '__main__':
    session = requests.session()
    login_xadmin(session)
    # login(session)
    # url2 = 'http://49.235.92.12:9000/api/v1/userinfo/'
    # res = session.get(url2)
    # print(res.text)





