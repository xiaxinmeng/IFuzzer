class BadEncoder():
    def encode(self, dummy):
        return 42
def _get_bad_encoder(dummy):
    return BadEncoder()

quopri = codecs.lookup("quopri")
quopri._is_text_encoding = True
quopri.incrementalencoder = _get_bad_encoder
t = io.TextIOWrapper(io.BytesIO(b'foo'), encoding="quopri")
t.write('bar')