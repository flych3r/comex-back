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

setup-dev-db: venv
	pipenv run python -m app table_file_to_db input/d_sh2.xlsx d_sh2 --xlsx
	pipenv run python -m app table_file_to_db input/d_via.xlsx d_via --xlsx
	pipenv run python -m app table_file_to_db input/f_comex.csv f_comex

setup-heroku-db: venv
	DATABASE_URL=$$(heroku config:get DATABASE_URL) pipenv run python -m app table_file_to_db input/d_sh2.xlsx d_sh2 --xlsx
	DATABASE_URL=$$(heroku config:get DATABASE_URL) pipenv run python -m app table_file_to_db input/d_via.xlsx d_via --xlsx
	DATABASE_URL=$$(heroku config:get DATABASE_URL) pipenv run python -m app table_file_to_db input/f_comex.csv f_comex
