info:
		poetry run gendiff --help

lint:
		poetry run flake8 gendiff

check: lint


build: check
		poetry build


