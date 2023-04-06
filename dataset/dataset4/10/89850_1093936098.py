class Pickler(pickle.Pickler):
  def persistent_id(self, obj):
    return super().persistent_id(obj)