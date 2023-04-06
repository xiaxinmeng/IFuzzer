import unicodedata
def bad_normalize(*args):
    return None

unicodedata.normalize = bad_normalize
import ast
ast.parse('\u03D5')