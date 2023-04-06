def dump_bytes(*args, **kwargs):
  return dumps(*args, **kwargs).encode('utf-8')