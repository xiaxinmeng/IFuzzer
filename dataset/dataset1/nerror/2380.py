try:
   raise ValueError
except ((ValueError,object),):
   pass
