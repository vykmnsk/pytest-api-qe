import os
import pytest
import requests


API_URL = os.getenv('TEST_API_URL')


@pytest.fixture(scope='session')
def get_response():
    return requests.get(API_URL)


@pytest.fixture(scope='session')
def post_response():
    return requests.post(API_URL, json={})
