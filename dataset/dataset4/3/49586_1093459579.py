def _asdict(self):
  'Return a new dict which maps field names to their values'
  return {'id': self[0], 'date': self[1], 'name': self[2], 'desc': self
[3]}