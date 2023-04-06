content = sys.stdin.buffer.read()
raw = io.BytesIO(content)
buffer = io.BufferedReader(raw)
encoding, _ = detect_encoding(buffer.readline)
buffer.seek(0)
text = TextIOWrapper(buffer, encoding)
# use text