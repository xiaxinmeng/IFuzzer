SAMPLES = (
  ('unicode', u''),
  ('bytes', ''),
  ('buffer', buffer('')),
# ('bytearray', bytearray('')),     # unsupported
# ('memoryview', memoryview(''))    # unsupported
)

import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('create table test(s varchar, b blob)')
c.executemany('insert into test(s, b) values (?, ?)', SAMPLES)
c.execute('select s, b from test')
print('\n'.join(str(l) for l in c.fetchall()))