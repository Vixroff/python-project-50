from gendiff.format.stylish import format_stylish
from gendiff.format.plain import format_plain
from gendiff.format.json import format_json


def format_diff(tree, format):
    if format == 'stylish':
        return format_stylish(tree)
    elif format == 'plain':
        return format_plain(tree)
    elif format == 'json':
        return format_json(tree)
