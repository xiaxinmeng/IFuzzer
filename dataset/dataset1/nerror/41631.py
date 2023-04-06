import _testcapi
import _ast
res = _testcapi.run_in_subinterp("import _ast; _ast.AST.x = 1")
if res != 0:
    raise Exception("bug")
print(_ast.AST.x)
