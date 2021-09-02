# API SQL Tutorials

Tutorials on using TOKU Systems API-SQL to work with data from IIoT sensors

## Running server locally

## Running with Python

1. Setup [pyenv](https://github.com/pyenv/pyenv).
1. Install required version of python.

	```bash
	pyenv install
	```

1. Setup [venv](https://docs.python.org/3/library/venv.html).

	```bash
	python -m venv .venv
	```

1. Activate virtual environment.

	```bash
	source .venv/bin/activate
	```

	Use `deactivate` from the command line to deactivate the virutal environment.

1. Install dependencies

	```bash
	pip install -r requirements.txt
	```

1. Start mkdocs.

	```bash
	mkdocs serve
	```

1. [Open browser](http://localhost:8000)
