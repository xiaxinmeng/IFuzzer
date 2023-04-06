src = """
f1 = lambda x=1: x
f2 = lambda x=2: x
"""

from dis import dis
c = compile(src, 'example', 'exec')
dis(c)