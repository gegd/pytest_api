from lxml import etree
import allure


@allure.step('获取添加的结果')
def get_add_result(result, x_path):
    demo = etree.HTML(result.text)
    nodes = demo.xpath(x_path)
    print(nodes[0].text)
    return nodes[0].text