ct = create_generator()
try:
    ct.next()
finally:
    ct.close()

from contextlib import closing
with closing(create_generator()) as ct:
    ct.next()