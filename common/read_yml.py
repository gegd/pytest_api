import os
import yaml


def read_yaml_file(yaml_path):
    if not os.path.isfile(yaml_path):
        raise FileNotFoundError('文件路径不正确')

    with open(yaml_path, 'r', encoding='utf-8') as f:
        cfg = f.read()
        data = yaml.load(cfg, Loader=yaml.FullLoader)
        return data


if __name__ == '__main__':
    real_path = os.path.realpath(__file__)
    yaml_path = os.path.join(os.path.dirname(real_path), 'req_data.yml')
    print(yaml_path)
    res = read_yaml_file(yaml_path)
    print(res['update_sex'])