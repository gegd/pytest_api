from case.xadmin_login import add_teacher
from common.html_re import get_add_result
from common.read_yml import read_yaml_file
import os
import allure
import pytest

real_path = os.path.realpath(__file__)
yaml_path = os.path.join(os.path.dirname(real_path), 'add_data.yml')
print('*******'+yaml_path)
add_data = read_yaml_file(yaml_path)['add_teacher']
add_data1 = read_yaml_file(yaml_path)['add_teacher1']


@allure.feature('新增teacher')
class TestAddTeacher(object):
    @allure.story('参数完整，新增成功')
    @pytest.mark.parametrize('teacher_name,tel,mail,sex,expect', add_data)
    def test_add_teacher001(self, login_xadmin_fix, del_before_login, teacher_name, tel, mail, sex, expect):
        """
        新增老师用例，参数完整
        :param login_xadmin_fix:
        :param del_before_login:
        :param teacher_name:
        :param tel:
        :param mail:
        :param sex:
        :param expect:
        :return:
        """
        res = add_teacher.teacher_add(login_xadmin_fix, teacher_name, tel, mail, sex)
        # print(res.text)
        x_path = "//*[@class='table table-bordered table-striped table-hover']/tbody/tr[1]/td[2]/a"
        acture_res = get_add_result(res, x_path)
        assert acture_res == expect

    @allure.story('姓名为空，新增失败')
    @pytest.mark.parametrize('teacher_name,tel,mail,sex,expect', add_data1)
    def test_add_teacher002(self, login_xadmin_fix, del_before_login, teacher_name, tel, mail, sex, expect):
        """
        新增老师用例,姓名为空
        :param login_xadmin_fix:
        :param del_before_login:
        :param teacher_name:
        :param tel:
        :param mail:
        :param sex:
        :param expect:
        :return:
        """
        res = add_teacher.teacher_add(login_xadmin_fix, teacher_name, tel, mail, sex)
        # print(res.text)
        x_path = "//*[@class='table table-bordered table-striped table-hover']/tbody/tr[1]/td[2]/a"
        acture_res = get_add_result(res, x_path)
        assert acture_res == expect


# if __name__ == '__main__':
#     pytest.main()

