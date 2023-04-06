import json
assert '\udb0a\udfdf' == json.loads(json.dumps('\udb0a\udfdf', ensure_ascii=False))