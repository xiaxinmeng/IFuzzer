def z0():
  c = a + 2

def z1():
  a = a + 2 # crash will happen here

a = 10

z0()
z1()