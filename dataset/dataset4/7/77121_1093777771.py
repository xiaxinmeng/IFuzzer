import re
import timeit

class ParseMap(dict):
    def __missing__(self, key): return 120  # ord('x')

trans = ParseMap((i,120) for i in range(128))
trans.update((ord(c), ord('(')) for c in "({[")
trans.update((ord(c), ord(')')) for c in ")}]")
trans.update((ord(c), ord(c)) for c in "\"'\\\n#")

trans_re = re.compile(r'''[^(){}\[]"'\\\n#]+''')
code='\t a([{b}])b"c\'d\n'*1000  # n = 1, 10, 100, 1000