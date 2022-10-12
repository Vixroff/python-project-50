from gendiff.format.stylish import format_stylish
from gendiff.format.plain import format_plain


def format_diff(tree, format):
    if format == 'stylish':
        return format_stylish(tree)
    elif format == 'plain':
        return format_plain(tree)
    else:
        pass
