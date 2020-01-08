from case.common_function import login
from common.connect_mysql import DbConnect
import requests
import pytest


@pytest.fixture(scope="module")
def login_fix():
    """获取个人信息之前，先要登录，自定义一个login"""
    print('先登录')
    session = requests.session()
    login(session)
    return session


@pytest.fixture(scope="function")
def unlogin_fix():
    """获取个人信息之前，先要登录，自定义一个login"""
    print('不登录')
    session = requests.session()
    session.headers.update({
        'Authorization': 'Token 7680a6193946e0a19333ca4b6cacb26fd8994cdbxxx'
    })
    return session


@pytest.fixture()
def do_register_del():
    connect = DbConnect('apps')
    delete_sql = "delete from auth_user where username = 'test1124'"
    connect.execute(delete_sql)