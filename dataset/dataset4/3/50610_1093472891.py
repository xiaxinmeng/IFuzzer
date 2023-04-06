import io

def test(buf):
   textio = io.TextIOWrapper(buf)

buf = io.BytesIO()
test(buf)
print(buf.closed)  # This prints True currently