import re
import os
from requests_toolbelt import MultipartEncoder
from common.html_re import get_add_result


def test_add_image(login_xadmin_fix, del_image):
    url = os.environ['xadmin_host'] + '/xadmin/hello/fileimage/add/'
    res = login_xadmin_fix.get(url)
    token = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", res.text)
    data = MultipartEncoder(
        fields=[
            ("csrfmiddlewaretoken", token[0]),
            ("csrfmiddlewaretoken", token[0]),
            ("title", "file_image_001"),
            ("image", ("aaa.png", open("D:\\aaa.png", "rb"), "image/png")),
            ("fiels", ("pom.xml", open("D:\\AutoTest\\pom.xml", "rb"), "image/png")),
            ("_save", "")
        ]
    )
    result = login_xadmin_fix.post(url=url, data=data, headers={'Content-Type': data.content_type})
    x_path = "//*[@class='table table-bordered table-striped table-hover']/tbody/tr[1]/td[2]/a"
    acture = get_add_result(result, x_path)
    assert acture == 'file_image_001'
