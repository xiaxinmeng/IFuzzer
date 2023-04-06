
from lib2to3.pgen2 import driver
from lib2to3 import pytree
from lib2to3 import pygram

_GRAMMAR_FOR_PY3 = pygram.python_grammar_no_print_statement.copy()
parser_driver = driver.Driver(_GRAMMAR_FOR_PY3, convert=pytree.convert)
tree = parser_driver.parse_string('100_1\n', debug=False)
