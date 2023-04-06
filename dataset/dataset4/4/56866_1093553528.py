def default(obj):  # pass to default parameter of json.dumps
  if isinstance(obj, frozenset):
    return {'_class': 'set', 'items': list(obj)}
  ...

def object_hook(obj):  # pass to object_hook parameter of json.loads
  if obj.get('_class') == 'set':
    return set(decoded_dict['items'])
  ...