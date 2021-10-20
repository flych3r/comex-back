help:
	@echo "available commands"
	@echo " - venv              : creates the development environment"
	@echo " - clean             : clean temporary folders and files"
	@echo " - lint              : checks code style and type checks"
	@echo " - run-dev           : runs api in development mode"

venv:
	pipenv sync --dev

clean:
	rm -rf `find . -type d -name .pytest_cache`
	rm -rf `find . -type d -name .mypy_cache`
	rm -rf `find . -type d -name __pycache__`
	rm -rf `find . -type d -name .ipynb_checkpoints`
	rm -f .coverage

lint: venv clean
	pipenv run flake8
	pipenv run mypy --install-types --non-interactive

run-dev: venv
	LOG_LEVEL=DEBUG pipenv run uvicorn app.main:app --reload

