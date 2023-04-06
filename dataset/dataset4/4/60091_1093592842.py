if isinstance(query, (str, bytes)):
  if len(query): raise TypeError("non empty strings not allowed")
  else: return query