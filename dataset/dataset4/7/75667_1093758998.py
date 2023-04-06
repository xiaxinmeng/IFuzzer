import json.encoder
class BadDict(dict):
    def items(self):
        return ()

encoder = json.encoder.c_make_encoder(None, None, None, None, 'foo', 'bar',
                                      True, None, None)
encoder(obj=BadDict({'spam': 42}), _current_indent_level=4)