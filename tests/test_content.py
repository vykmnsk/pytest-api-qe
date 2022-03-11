import common


def test_model_musicfestival(get_response):
    jcontent = extract_json(get_response)
    for festival in jcontent:
        name = festival.get('name')
        assert name and name.strip(), f"Expect name in festival={festival}"
        bands = festival.get('bands')
        assert bands, f"Expect bands in festival={festival}"


def test_model_band(get_response):
    jcontent = extract_json(get_response)
    for festival in jcontent:
        bands = festival.get('bands')
        assert bands, f"Expect bands in festival={festival}"
        for band in bands:
            name = band.get('name')
            assert name and name.strip(), f"Expect name in band={band}"
            rec_label = band.get('recordLabel')
            assert rec_label and rec_label.strip(), f"Expect recordLabel in band={band}"


def extract_json(get_response):
    jcontent = common.parse_json(get_response)
    assert type(jcontent) == list, \
        f"Expect JSON list in response={get_response.text[0:1000]}"
    return jcontent
