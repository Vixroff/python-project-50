install:
		poetry install

lint:
		poetry run flake8 gendiff

test:
		poetry run pytest

test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml

check: lint test cov


build: check
		poetry build

run:
		poetry run gendiff --format json tests/fixtures/file1_tree.json tests/fixtures/file2_tree.json
