if isinstance(data, types.FileType):
  return data.read()
else:
  return str(data)