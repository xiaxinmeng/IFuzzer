import json
unicode_bytes = '\xed\xa8\x80'
unicode_string = unicode_bytes.decode("utf8")
json_encoded = json.dumps(unicode_string, ensure_ascii=False)