import json
import pytest


def test_response_code(get_response):
    assert get_response.ok


def test_response_not_empty(get_response):
    assert get_response.content, 'empty response'


def test_response_is_json(get_response):
    parse_json(get_response)


def test_response_headers(get_response):
    expected_content_types = [
        'application/json',
        'application/json; charset=utf-8',
        'text/json; charset=utf-8']
    content_type = get_response.headers['Content-Type']
    assert content_type.lower() in expected_content_types, \
        f"Response Content Type '{content_type}' is expected to be JSON"


def test_response_content(get_response):
    jcontent = parse_json(get_response)
    assert 'name' in jcontent
    assert 'bands' in jcontent


def test_post_call_rejected(post_response):
    assert not post_response.ok


def parse_json(resp):
    try:
        result = json.loads(resp.content)
    except ValueError:
        pytest.fail(f'response is not JSON: {resp.text[0:1000]}')
    return result
