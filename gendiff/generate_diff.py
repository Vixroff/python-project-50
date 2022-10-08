import json


def make_lower_bools(dict):
    for key, value in dict.items():
        if type(value) is bool:
            value = str(value).lower()
            dict[key] = value
    return dict


def open_json(json_file):
    return json.load(open(json_file))


def generate_diff(first_file, second_file, format=None):
    file1 = make_lower_bools(open_json(first_file))
    file2 = make_lower_bools(open_json(second_file))
    keys1, keys2 = file1.keys(), file2.keys()
    keys = sorted(keys1 | keys2)
    result = ['{']
    for key in keys:
        if key in keys1 and key in keys2:
            if file1[key] == file2[key]:
                result.append('    {}: {}'.format(key, file1[key]))
            else:
                result.append('  - {}: {}'.format(key, file1[key]))
                result.append('  + {}: {}'.format(key, file2[key]))
        elif key not in keys1:
            result.append('  + {}: {}'.format(key, file2[key]))
        elif key not in keys2:
            result.append('  - {}: {}'.format(key, file1[key]))
    result.append('}')
    result = '\n'.join(result)
    return result


if __name__ == "__main__":
    pass
