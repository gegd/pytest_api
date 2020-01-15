from requests_toolbelt import MultipartEncoder
import re
import os
import allure


@allure.step('添加老师接口')
def teacher_add(session, teacher_name, tel, mail, sex):
    """
    新增老师接口,teacher_name, tel, mail, sex, expect这几个请求参数做了参数化
    :param login_xadmin_fix:
    :param del_before_login:
    :param teacher_name:
    :param tel:
    :param mail:
    :param sex:
    :return:
    """
    url = os.environ['xadmin_host'] + '/xadmin/hello/teacherman/add/'
    res1 = session.get(url)
    token = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", res1.text)
    print(token[0])
    data = MultipartEncoder(
        fields=[
            ("csrfmiddlewaretoken", token[0]),
            ("csrfmiddlewaretoken", token[0]),
            ("teacher_name", teacher_name),
            ("tel", tel),
            ("mail", mail),
            ("sex", sex),
            ("_save", "")
        ]
    )
    res = session.post(url=url, data=data, headers={'Content-Type': data.content_type})
    return res