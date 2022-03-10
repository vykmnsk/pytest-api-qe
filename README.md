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

## Configure
set API endpoint URL in environment variable (Mac, Linux):

    export TEST_API_URL=https://...

or on Windows:

    set TEST_API_URL=https://...

## Run
#### All tests

    pytest

#### All tests with debugger on error

    pytest --pdb

#### Deactivate virtual environment when finished

    deactivate
