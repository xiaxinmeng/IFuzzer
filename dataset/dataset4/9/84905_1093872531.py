def foo(exc):
   try:
       1/0
   except Exception as exc:
       ...
   finally:
       return exc

foo(1)