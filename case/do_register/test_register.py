import requests
import pytest


def test_register_001(do_register_del):
    """注册成功"""
    s = requests.session()
    url = 'http://49.235.92.12:9000/api/v1/register'

    body = {
        'username': 'test1124',
        'password': '123456',
        'mail': '1233@qq.com'
    }

    res = s.post(url, json=body)
    print(res.json())
    assert res.json()['msg'] == '注册成功!'
    assert res.json()['code'] == 0


def test_register_002():
    """重复注册"""
    s = requests.session()
    url = 'http://49.235.92.12:9000/api/v1/register'

    body = {
        'username': 'test1124',
        'password': '123456',
        'mail': '1233@qq.com'
    }

    res = s.post(url, json=body)
    res1 = s.post(url, json=body)
    print(res1.json())
    assert res1.json()['msg'] == '注册成功!'
    assert res1.json()['code'] == 0


if __name__ == '__main__':
    pytest.main(['-s', 'test_register.py'])