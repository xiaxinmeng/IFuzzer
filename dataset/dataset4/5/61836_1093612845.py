#module foo.B
A = __import__(".", fromlist=["A"]).A

#module foo.A
B = __import__(".", fromlist=["B"]).B