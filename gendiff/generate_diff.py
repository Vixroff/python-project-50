from gendiff.format.format import format_diff
from gendiff.tools.tree import get_diff_tree
from gendiff.tools.reader import read


def generate_diff(first_file, second_file, format):
    file1, file2 = read(first_file), read(second_file)
    diff = get_diff_tree(file1, file2)
    result = format_diff(diff, format)
    print(result)
    return result


if __name__ == "__main__":
    pass
