from case.common_function import login_xadmin
from common.connect_mysql import DbConnect
import requests
import pytest
import allure


@allure.step('登录xadmin')
@pytest.fixture(scope="session")
def login_xadmin_fix(request):
    """新增老师前先登录"""
    print('先登录')
    s = requests.session()
    login_xadmin(s)

    def close_s():#关闭session
        s.close()
    request.addfinalizer(close_s)
    return s


@pytest.fixture(scope='module')
def del_before_login():
    '''新增老师前先删除数据'''
    db = DbConnect('djangoweb')
    delete_sql = "DELETE FROM hello_teacher WHERE teacher_name = 'yoyo002'"
    db.execute(delete_sql)
    db.close()


@pytest.fixture(scope='module')
def del_image():
    '''新增图片前先删除'''
    db = DbConnect('djangoweb')
    delete_sql = "DELETE FROM hello_fileimage WHERE title = 'file_image_001'"
    db.execute(delete_sql)
    db.close()