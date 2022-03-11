import common


def test_response_code(get_response):
    assert get_response.ok


def test_response_not_empty(get_response):
    assert get_response.text, 'Expect non-empty response'


def test_response_is_json(get_response):
    common.parse_json(get_response)


def test_response_headers(get_response):
    expected_content_types = [
        'application/json',
        'application/json; charset=utf-8',
        'text/json; charset=utf-8']
    content_type = get_response.headers['Content-Type']
    assert content_type.lower() in expected_content_types, \
        f"Response Content Type '{content_type}' is expected to be JSON"
