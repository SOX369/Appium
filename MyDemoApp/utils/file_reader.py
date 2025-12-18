import yaml
import os

def load_yaml_data(yaml_file_name):
    """
    读取 config 目录下的 yaml 文件
    return: List[Dict]
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "config", yaml_file_name)

    with open(data_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data