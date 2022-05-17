
fmt: unify isort black

unify:
	unify --in-place --recursive .

isort:
	isort .

black:
	black .

.PHONY: fmt unify isort black

lint: flake8 pylint bandit mypy

flake8:
	flake8 .

pylint:
	pylint {{ cookiecutter.directory_name }}.py

bandit:
	bandit -c pyproject.toml .

mypy:
	mypy .

.PHONY: lint flake8 pylint bandit mypy

docs:
	make -C docs html

.PHONY: docs

tests:
	pytest tests

.PHONY: tests
