import pytest
from gendiff import generate_diff


@pytest.mark.parametrize(
    "file1, file2, format, expected",
    [
        ('tests/fixtures/file1_plain.json', 'tests/fixtures/file2_plain.json', 'stylish', 'tests/fixtures/json_plain_stylish_expected.txt'),
        ('tests/fixtures/file1_plain.yaml', 'tests/fixtures/file2_plain.yml', 'stylish', 'tests/fixtures/yaml_plain_stylish_expected.txt'),
        ('tests/fixtures/file1_tree.json', 'tests/fixtures/file2_tree.json', 'stylish', 'tests/fixtures/json_tree_stylish_expected.txt'),
        ('tests/fixtures/file1_tree.json', 'tests/fixtures/file2_tree.json', 'plain', 'tests/fixtures/json_tree_plain_expected.txt'),
        ('tests/fixtures/file1_tree.json', 'tests/fixtures/file2_tree.json', 'json', 'tests/fixtures/json_tree_json_expected.txt')
    ]
)
def test_generate_diff(file1, file2, format, expected):
    output = generate_diff(file1, file2, format)
    with open(expected) as f:
        expected_output = f.read()
    assert output == expected_output
