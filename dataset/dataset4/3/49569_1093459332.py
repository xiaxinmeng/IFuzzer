def main():
   try:
       thing()
   except SomethingChanged:
       exit(1)
   except BinaryDiff:
       exit(2)
   except:
       exit(3)