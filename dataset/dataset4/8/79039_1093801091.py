class MappingProxyEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, MappingProxyType):
      return obj.copy()
    return JSONEncoder.default(self, obj)