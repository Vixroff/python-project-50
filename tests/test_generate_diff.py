from gendiff.generate_diff import generate_diff


def test_generate_diff():
    output = generate_diff(
        'tests/fixtures/file1_plain.json',
        'tests/fixtures/file2_plain.json'
    )
    with open('tests/fixtures/json_plain_expected.txt') as f:
        expected_output = f.read()
    assert output == expected_output
