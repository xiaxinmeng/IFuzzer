from __future__ import generators

def f():
    for i in range(3):
        try:
            continue
        finally:
            yield 1

g = f()
print(g.next())
print(g.next())

 	  	 
