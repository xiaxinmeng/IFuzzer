import ast
source = """\
[interesting
foo()
"""
print(repr(source))
compile(source, "", "exec")