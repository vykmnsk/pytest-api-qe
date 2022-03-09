# API Integration tests

## Setup

Download and run _Python 3.x (64 bit)_ executable installer from [python.org](https://www.python.org/downloads/release/python-386/)

Verify python/pip are installed:

    python --version
    pip --version

 Create, activate a virtual environment and install python libs (Windows CMD)

    python -m venv .venv
    .venv\Scripts\activate.bat
	pip install --upgrade pip
	pip install -r reqs.txt

## Run tests

### on Local machine

#### All tests

    pytest

#### All tests with debugger on error

    pytest --pdb

#### Deactivate virtual environment when finished

    deactivate
