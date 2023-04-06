if os.name in ('nt', 'ce'):
   def atomic_rename(a, b):
      if os.path.exists(b):
         unlink(b)
      rename(a, b)
else:
   atomic_rename = os.rename