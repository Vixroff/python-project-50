from gendiff.format.stylish import format_stylish


def format_diff(tree, format):
    if format == 'stylish':
        return format_stylish(tree)
    else:
        pass
