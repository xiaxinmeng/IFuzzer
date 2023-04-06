import codecs
import io

rot13 = codecs.lookup("rot13")
rot13._is_text_encoding = True
t = io.TextIOWrapper(io.BytesIO(b'foo'), encoding="rot13")
t.write('bar')