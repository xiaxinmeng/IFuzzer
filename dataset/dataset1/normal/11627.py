class Foo(Exception):
 def __new__(*args):
  return object()
 
try:
 raise Foo
except Exception as e:
 print ('got it', e)
