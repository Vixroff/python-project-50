def check_value(value):
    if isinstance(value, str):
        value = "'{}'".format(value)
    elif isinstance(value, dict):
        value = "[complex value]"
    elif value is False:
        value = 'false'
    elif value is True:
        value = 'true'
    elif value is None:
        value = 'null'
    return value


def format_plain(tree, key=''):
    value = []
    for node in tree:
        dir = '.'.join([key, node['key']])
        if node['status'] == 'nested':
            value.append(
                format_plain(node['value'], dir)
            )
        elif node['status'] == 'added':
            value.append("Property '{}' was added with value: {}".format(
                dir[1:], check_value(node['value'])
            )
            )
        elif node['status'] == 'deleted':
            value.append("Property '{}' was removed".format(dir[1:]))
        elif node['status'] == 'changed':
            value.append("Property '{}' was updated. From {} to {}".format(
                dir[1:], check_value(node['value'][0]), check_value(node['value'][1])
            )
            )
        else:
            continue
    return '\n'.join(value)
