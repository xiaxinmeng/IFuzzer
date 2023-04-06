import compiler
a="""def foo(*x): return x
foo((a for b in [[1,2,3],[4,5,6]] for a in b),'Z')"""
compiler.compile(a,'<string>', 'exec')