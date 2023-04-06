
import ast

globalsDict = {}

fAst = ast.FunctionDef(
	name="foo",
	args=ast.arguments(
		args=[], vararg=None, kwarg=None, defaults=[],
		kwonlyargs=[], kw_defaults=[]),
	body=[], decorator_list=[])

exprAst = ast.Interactive(body=[fAst])
ast.fix_missing_locations(exprAst)
compiled = compile(exprAst, "<foo>", "single")
eval(compiled, globalsDict, globalsDict)

print(globalsDict["foo"])
