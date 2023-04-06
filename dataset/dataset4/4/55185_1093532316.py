import json

print(json.loads('123'))
# 123

print(json.loads(b'123'))
# /Library/Frameworks/Python.framework/Versions/3.1/lib/python3.1/json/decoder.py:325:  
#   TypeError: can't use a string pattern on a bytes-like object

print(json.loads(b'123', encoding='utf-8'))
# /Library/Frameworks/Python.framework/Versions/3.1/lib/python3.1/json/decoder.py:325:  
#   TypeError: can't use a string pattern on a bytes-like object