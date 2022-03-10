import common


def test_response_content(get_response):
    jcontent = common.parse_json(get_response)
    assert 'name' in jcontent
    assert 'bands' in jcontent
