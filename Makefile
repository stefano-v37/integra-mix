
SRC_DIR = src
AUTOFLAKE_OPTS = -r -i --ignore-init-module-imports --expand-star-imports --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables

.PHONY: autoflake
autoflake:
	autoflake $(AUTOFLAKE_OPTS) $(SRC_DIR)

.PHONY: black
black:
	black $(SRC_DIR)

.PHONY: check-python
check-python:
	$(eval PYTHON_VERSION := $(shell python --version 2>&1 | cut -d ' ' -f 2))
	@if [ "$(PYTHON_VERSION)" != "3.11.6" ]; then \
		echo "Error: Python 3.11.6 is required, but $(PYTHON_VERSION) is installed."; \
		exit 1; \
	fi
	@echo "Python version is correct."

.PHONY: create-venv
create-venv: check-python
	python -m venv venv

.PHONY: format
format: autoflake black isort

.PHONY: install-requirements
install-requirements: check-python
	pip install pip --upgrade
	pip install --upgrade -r requirements.txt

.PHONY: install
install: check-python
	pip install -e .

.PHONY: isort
isort:
	isort $(SRC_DIR)