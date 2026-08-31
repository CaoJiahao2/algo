PYTHON ?= python3.12

.PHONY: test

test:
	$(PYTHON) -m pytest -q
