from __future__ import nested_scopes

def t1(n):
    def t2(): return n
    return t2

f = t1(5)
exec(f.func_code)

 	  	 
