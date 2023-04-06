def _is_legal_key(key):
    return key and set(_LegalChars).issuperset(key)