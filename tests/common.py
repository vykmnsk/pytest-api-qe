import json
import pytest


def parse_json(resp):
    try:
        result = json.loads(resp.content)
    except ValueError:
        pytest.fail(f'response is not JSON: {resp.text[0:1000]}')
    return result
