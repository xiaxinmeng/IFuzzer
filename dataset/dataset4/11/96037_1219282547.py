
try:
   raise TimeoutError
finally:
   try:
       raise ValueError
   except:
       1/0
