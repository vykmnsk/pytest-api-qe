import os
import json
import pytest
import requests


API_URL = os.getenv('TEST_API_URL')



def test_response_code():
    resp = call_get()
    assert resp.ok


def test_response_not_empty():
    resp = call_get()
    assert resp.content, 'empty response'


def test_response_is_json():
    resp = call_get()
    parse_json(resp)


def test_response_content():
    resp = call_get()
    jcontent = parse_json(resp)
    assert jcontent['surname']


def test_post_call_rejected():
    resp = call_post()
    assert not resp.ok


def call_get():
    return requests.get(API_URL)


def call_post():
    return requests.post(API_URL, data={})


def parse_json(resp):
    try:
        result = json.loads(resp.content)
    except ValueError:
        pytest.fail(f'response is not JSON: {resp.text[0:1000]}')
    return result
