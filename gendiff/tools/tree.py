def get_diff_tree(file1, file2):
    keys1, keys2 = file1.keys(), file2.keys()
    keys = sorted(keys1 | keys2)
    tree = []
    for key in keys:
        if key not in keys1:
            child = {
                'status': 'added',
                'key': key,
                'value': file2[key]
            }
        elif key not in keys2:
            child = {
                'status': 'deleted',
                'key': key,
                'value': file1[key]
            }
        elif file1[key] == file2[key]:
            child = {
                'status': 'unchanged',
                'key': key,
                'value': file1[key]
            }
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            child = {
                'status': 'nested',
                'key': key,
                'value': get_diff_tree(file1[key], file2[key])
            }
        else:
            child = {
                'status': 'changed',
                'key': key,
                'value': [file1[key], file2[key]]
            }
        tree.append(child)
    return tree
