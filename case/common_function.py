import requests


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


if __name__ == '__main__':
    session = requests.session()
    login(session)

    url2 = 'http://49.235.92.12:9000/api/v1/userinfo/'
    res = session.get(url2)
    print(res.text)





