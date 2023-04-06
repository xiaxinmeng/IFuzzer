import sys
import types

program = bytes([
	100, 0, 0,  # LOAD_CONST 0
	83,         # RETURN_VALUE
	])

varnames = ()

# Uncomment the next line to make the crash go away
# varnames = ('x',)

code_object = types.CodeType(
	1,       # argcount
	0,       # kwonlyargcount
	1,       # nlocals
	1,       # stacksize
	67,      # flags
	program, # codestring
	(None,), # constants
	(),      # names
	varnames,# varnames
	'<stdin>',# filename
	'',      # name (of function)
	1,       # firstlineno
	b'',     # lnotab
	(),      # freevars
	(),      # cellvars
	)

function = types.FunctionType(code_object, globals())
function()
