
from ast import *

globalsDict = {}

exprAst = Interactive(body=[
	FunctionDef(
		name=u'foo',
		args=arguments(args=[], vararg=None, kwarg=None, defaults=[]),
		body=[Pass()],
		decorator_list=[])])

fix_missing_locations(exprAst)
compiled = compile(exprAst, "<foo>", "single")
eval(compiled, {}, globalsDict)

f = globalsDict["foo"]
print(f)
