import io
_bytesio = io.BytesIO()

_bytesio.write(b'abc')
_bytesio.write(b'def')
_bytesio.seek(0)
_bytesio.write(b'xyz')

print(_bytesio.read(2))
print(_bytesio.read(2))
print(_bytesio.getvalue())