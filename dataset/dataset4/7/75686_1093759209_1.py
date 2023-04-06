import _json
def _bad_encoder(*args):
    return None

enc = _json.make_encoder(None, None, _bad_encoder, None,
                         'foo', 'bar', None, None, None)

enc(obj={'spam': 42}, _current_indent_level=4)