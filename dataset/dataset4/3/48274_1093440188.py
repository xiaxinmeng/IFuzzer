def cache_float(value):
   return abs(value) in (0.0, 1.0, 2.0)

def create_float(value):
   try:
      return cache[value]
   except KeyError:
      obj = float(value)
      if cache_value(value):
         cache[value] = obj
      return obj