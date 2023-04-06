class A:
 def __init__(self):
   print('created')

 def __del__(self):
   print('destroyed')

a = A()