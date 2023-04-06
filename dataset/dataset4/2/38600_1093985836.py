program = '''
import foo.bar as baz
'''

code1 = compile(program, 'foobar', 'exec')
code2 = compiler.compile(program, 'foobar', 'exec')