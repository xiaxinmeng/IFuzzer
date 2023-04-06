
from ast import *

globalsDict = {}

body = [
	Assign(targets=[Name(id=u'argc', ctx=Store())],
		   value=Name(id=u'None', ctx=Load())),
	]

exprAst = Interactive(body=[
	FunctionDef(
		name='foo',
		args=arguments(args=[Name(id=u'argc', ctx=Param()), Name(id=u'argv', ctx=Param())],
					   vararg=None, kwarg=None, defaults=[]),
		body=body,
		decorator_list=[])])

fix_missing_locations(exprAst)
compiled = compile(exprAst, "<foo>", "single")
eval(compiled, {}, globalsDict)

f = globalsDict["foo"]
print(f)
