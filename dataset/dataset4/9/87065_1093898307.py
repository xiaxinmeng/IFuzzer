b = B()
try:
   if b:
        pass
except AttributeError:
   print("GOT ERROR")
   raise IndexError("Should GET THIS")

print("SHOULDN'T GET THIS")