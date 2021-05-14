
# How to use this project to see effects of code changes:
# conda activate spasco
# pip install .
# spasco args



# ------------- Test/Lint  ------------------------------------

.PHONY: pre-commit pre-commit-update lint test test-all

pre-commit: ## apply pre-commit to all files
	pre-commit run --all-files

pre-commit-update: ## update pre-commit
	pre-commit autoupdate

lint: ## check style with flake8
	flake8 app tests

test: ## run tests quickly with the default Python
	pytest -v

test-all: ## test across Python 3.6 - 3.9
	tox



# ------------- Clean Test/Lint/Build Artifacts  ---------------------

.PHONY: clean clean-pyc clean-test clean-build

clean: clean-pyc clean-test clean-build ## remove all build, test and Python artifacts

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -fr .mypy_cache
	rm -fr .pytest_cache

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +



# ------------  Deployment  -----------------------------------

.PHONY: dist release

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

release: dist ## package and upload a release
	twine upload dist/*



# ------------  Help  --------------------------------------

.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help


