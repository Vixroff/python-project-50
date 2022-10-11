import json
import os
import yaml


def make_abspath(path):
    return os.path.abspath(path)


def read_json(json_path):
    return json.load(open(json_path))


def read_yaml(yaml_path):
    return yaml.safe_load(open(yaml_path))


def read(file):
    path = make_abspath(file)
    _, file_extension = os.path.splitext(path)
    if file_extension == '.json':
        return read_json(path)
    elif file_extension in ['.yml', '.yaml']:
        return read_yaml(path)
