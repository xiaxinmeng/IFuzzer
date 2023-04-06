import io
import pickle

class XPickler(pickle.Pickler):
  def persistent_id(self, obj):
    if obj is type(None):
      return "NoneType"
    return None

class XUnpickler(pickle.Unpickler):
  def persistent_load(self, persistent_id):
    if persistent_id == "NoneType":
      return type(None)

def dumps(obj):
    f = io.BytesIO()
    XPickler(f).dump(obj)
    return f.getvalue()

def loads(s):
    return XUnpickler(io.BytesIO(s)).load()