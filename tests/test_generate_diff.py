import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize(
    "file1, file2, expected",
    [
        ('tests/fixtures/file1_plain.json', 'tests/fixtures/file2_plain.json', 'tests/fixtures/json_plain_expected.txt'),
        ('tests/fixtures/file1_plain.yaml', 'tests/fixtures/file2_plain.yml', 'tests/fixtures/yaml_plain_expected.txt' )
    ]
)


def test_generate_diff(file1, file2, expected):
    output = generate_diff(file1, file2)
    with open(expected) as f:
        expected_output = f.read()
    assert output == expected_output
