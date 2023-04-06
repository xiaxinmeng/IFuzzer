import ast
code = """\
x = (
        'PERL_MM_OPT', (
            f'wat'
            f'INSTALL-BASE={shlex.quote(venv)} '
            f'wat'
        ),
)
"""
elem = ast.parse(code).body[0].value.elts[1].values[1].value
print(elem)
print(code.split("\n")[elem.lineno-1][elem.col_offset:elem.end_col_offset])