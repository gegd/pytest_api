
def test_info_001(login_fix):
    """传入正确的token"""
    url = 'http://49.235.92.12:9000/api/v1/userinfo/'
    res = login_fix.get(url)
    print(res.text)
    assert res.json()['msg'] == 'sucess!'
    assert res.json()['code'] == 0


def test_info_002(unlogin_fix):
    """传入非法的token"""
    url = 'http://49.235.92.12:9000/api/v1/userinfo/'
    res = unlogin_fix.get(url)
    print(res.text)
    assert res.status_code == 401
