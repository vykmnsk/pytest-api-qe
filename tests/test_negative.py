def test_post_call_rejected(post_response):
    assert not post_response.ok
