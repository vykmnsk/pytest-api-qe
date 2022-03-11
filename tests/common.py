import json
import pytest


def parse_json(resp):
    try:
        jcontent = json.loads(resp.content)
    except ValueError:
        pytest.fail(f"Expect JSON in response={resp.text[0:1000]}")

    assert jcontent, "Expect non-empty response"
    return jcontent
