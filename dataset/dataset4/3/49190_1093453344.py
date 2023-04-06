a = input()
try:
   int(a) # or float(a)
except ValueError:
   print("Bad input")