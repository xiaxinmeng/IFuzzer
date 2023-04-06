#module foo.B
A = __import__(".A")

#module foo.A
B = __import__(".B")