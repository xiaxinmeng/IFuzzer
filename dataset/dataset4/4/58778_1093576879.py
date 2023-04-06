class RawJSON(str): pass

origEnc = json.encoder.encode_basestring_ascii
def rawEnc(obj):
  if isinstance(obj, RawJSON):
    return obj
  return origEnc(obj)
json.encoder.encode_basestring_ascii = rawEnc