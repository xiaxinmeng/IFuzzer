import time
class C:
 def __getitem__(self, i):
  raise IndexError
 def __len__(self):
  return 9

time.struct_time(C())
