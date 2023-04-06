class a(int):
   def __new__(cls,number):
     return int.__new__(cls,number)
for x in range(0,a(5)):
  print(x)