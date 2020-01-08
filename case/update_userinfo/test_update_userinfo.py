import pytest
import os
from common.read_yml import read_yaml_file

real_path = os.path.realpath(__file__)
yaml_path = os.path.join(os.path.dirname(real_path), 'req_data.yml')
print(yaml_path)
update_data = read_yaml_file(yaml_path)['update_sex']

# @pytest.mark.skip('阻塞bug')
@pytest.mark.appapi
@pytest.mark.parametrize('input_data,expect', update_data)
def test_update_userinfo_001(login_fix, input_data, expect):
    """修改本人性别信息"""
    url = 'http://49.235.92.12:9000/api/v1/userinfo/'
    params = {
        'name': 'test',
        'sex': input_data,
        'age': '20',
        'mail': '283340479@qq.com'
    }
    res = login_fix.post(url, json=params)
    print(res.text)
    assert res.json()['message'] == expect['message']
    assert res.json()['code'] == expect['code']


def test_update_userinfo_002(login_fix):
    """修改非本人信息"""
    url = 'http://49.235.92.12:9000/api/v1/userinfo/'
    params = {
        'name': 'testx',
        'sex': 'M',
        'age': '20',
        'mail': '283340479@qq.com'
    }
    res = login_fix.post(url, json=params)
    print(res.text)
    assert res.json()['message'] == '无权限操作'
    assert res.json()['code'] == 4000


if __name__ == '__main__':
    pytest.main(['-s', 'test_update_userinfo.py', '-m appapi'])
