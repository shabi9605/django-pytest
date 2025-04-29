# django-pytest

## What is this repository for

* Backend code for django-pytest.
* Version 0.1.0

## How do I get set up

All Python package dependencies are specified in `Pipfile` and `Pipfile.lock` instead of `requirements.txt` since we are using
[pipenv](https://pipenv.pypa.io/en/latest/). To install these packages use the following command

    pipenv install --dev

If you are using not `python3.7` use the following command instead

    pipenv install --dev --python python3.X

Where `X` should be replaced with which every version you are using

### Activate the environment

    pipenv shell

### How to run the local server

with the env active use following commands to run local server

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

Alternately, Use these commands if you don't want a active python env in your terminal

    pipenv run migrate
    pipenv run superuser
    pipenv run server

refer to the `Pipfile [scripts]` section for [more info](https://pipenv-fork.readthedocs.io/en/latest/advanced.html#custom-script-shortcuts)

### Other development tools

[flake8](https://flake8.readthedocs.io/en/latest/) - for linting and ensure python best practice are meet
[yapf](https://github.com/google/yapf) - for code formatting and provide consistent code styling




# 🧪 Django API Testing with Pytest

## ✅ Install Required Packages

```bash
pip install pytest pytest-django pytest-html djangorestframework djangorestframework-simplejwt
If using token authentication (classic DRF tokens):

bash
Copy
Edit
pip install djangorestframework authtoken
⚙️ Configure Pytest
Create a file named pytest.ini in your project root:

ini
Copy
Edit
[pytest]
DJANGO_SETTINGS_MODULE = your_project.settings
python_files = tests.py test_*.py *_tests.py
addopts = --reuse-db
log_cli = true
log_cli_level = INFO
log_format = %(asctime)s | %(levelname)s | %(name)s | %(message)s
log_date_format = %H:%M:%S
🧪 Run Tests
Run all tests with:

bash
Copy
Edit
pytest
Re-use the same test database (faster):

bash
Copy
Edit
pytest --reuse-db
🪵 Enable Logging in Terminal
Logs will automatically appear if log_cli = true is set in pytest.ini. Or use:

bash
Copy
Edit
pytest -o log_cli=true --log-cli-level=INFO
📝 Generate HTML Report
Create a portable HTML report:

bash
Copy
Edit
pytest --html=report.html --self-contained-html
Add metadata to the report:

bash
Copy
Edit
pytest --html=report.html --self-contained-html --metadata="Project: MyApp" --metadata="Tester: YourName"
✅ Summary of Commands

Task	Command
Run tests	pytest
Run with DB reuse	pytest --reuse-db
Show logs	pytest -o log_cli=true --log-cli-level=INFO
Generate HTML report	pytest --html=report.html --self-contained-html
Install all packages	pip install pytest pytest-django pytest-html djangorestframework