install:
		poetry install

lint:
		poetry run flake8 gendiff

test:
		poetry run pytest

check: lint test


build: check
		poetry build


