INDENT = {
    'basic': '    ',
    'prefix': '  '
}


def format_data(data, indent):
    if isinstance(data, dict):
        indent += INDENT['basic']
        result = '{\n'
        for key in data.keys():
            value = format_data(data[key], indent)
            result += '{}  {}: {}\n'.format(
                indent, key, value
            )
        result += indent[:-2] + '}'
    elif data is False:
        result = 'false'
    elif data is True:
        result = 'true'
    elif data is None:
        result = 'null'
    else:
        result = str(data)
    return result


def format_stylish(tree, level=0):
    result = '{\n'
    indent = INDENT['prefix'] + INDENT['basic'] * level
    for node in tree:
        if node['status'] == 'unchanged':
            node_format = '{}  {}: {}\n'.format(
                indent, node['key'], format_data(node['value'], indent)
            )
        elif node['status'] == 'deleted':
            node_format = '{}- {}: {}\n'.format(
                indent, node['key'], format_data(node['value'], indent)
            )
        elif node['status'] == 'added':
            node_format = '{}+ {}: {}\n'.format(
                indent, node['key'], format_data(node['value'], indent)
            )
        elif node['status'] == 'changed':
            node_format = '{}- {}: {}\n{}+ {}: {}\n'.format(
                indent, node['key'], format_data(node['value'][0], indent),
                indent, node['key'], format_data(node['value'][1], indent)
            )
        else:
            node_format = '{}  {}: {}\n'.format(
                indent, node['key'], format_stylish(node['value'], level + 1)
            )
        result += node_format
    result += indent[:-2] + '}'
    return result
