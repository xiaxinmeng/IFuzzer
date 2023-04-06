import re, sys
class Issue3328:
    def f(self):
        # unbalanced parenthesis
        x = re.compile('(123')

o = Issue3328()
sys.getrefcount(o)      # prints 2
o.f()
sys.getrefcount(o)      # prints 3