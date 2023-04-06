# Stops after the first hit since there should be at most one of each header in the dict
def _find_key_insensitive(d, key):
  key = key.lower()
  for key2 in d:
    if key2.lower() == key:
      return key2
  return None # Unnecessary, but explicit is better than implicit ;-)