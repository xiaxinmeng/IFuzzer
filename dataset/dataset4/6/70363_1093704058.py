import tempfile
import io
import json


with tempfile.SpooledTemporaryFile(max_size=2**20) as f:
    tf = io.TextIOWrapper(f, encoding='utf-8')
    json.dump({}, fp=tf)