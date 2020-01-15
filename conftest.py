import os
import pytest


def pytest_addoption(parser):
    """
    添加命令行配置参数
    """
    parser.addoption(
        "--cmdhost", action='store', default='http://49.235.92.12:8020',
        help='test host address'
    )


@pytest.fixture(scope='session', autouse=True)
def get_host(request):
    """
    获取命令行参数，给到环境变量
    :return:
    """
    os.environ['xadmin_host'] = request.config.getoption('--cmdhost')
    print('当前运行环境：%s' % os.environ['xadmin_host'])


