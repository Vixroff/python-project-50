import json
import os
import yaml


def make_abspath(path):
    return os.path.abspath(path)


def make_lower_bools(dict):
    for key, value in dict.items():
        if type(value) is bool:
            value = str(value).lower()
            dict[key] = value
    return dict


def read_json(json_path):
    return json.load(open(json_path))


def read_yaml(yaml_path):
    return yaml.safe_load(open(yaml_path))


def read(file):
    path = make_abspath(file)
    _, file_extension = os.path.splitext(path)
    if file_extension == '.json':
        return make_lower_bools(read_json(path))
    elif file_extension in ['.yml', '.yaml']:
        return make_lower_bools(read_yaml(path))
