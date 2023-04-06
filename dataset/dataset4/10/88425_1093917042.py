from lib2to3 import pygram, pytree
from lib2to3.pgen2 import driver
from lib2to3.pgen2.parse import ParseError

grammar = pygram.python_grammar.copy()
driver = driver.Driver(grammar, convert=pytree.convert)

strings = [
    "def fname(): pass",
    "def exec(): pass",
    """
class C:
    def exec(self): pass""",
]

for s in strings:
    try:
        driver.parse_string(s + '\n')
    except ParseError as pe:
        print("It fails:", s)
    else:
        print("It works:", s)
