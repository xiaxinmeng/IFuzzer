cursor.execute('SELECT value FROM test')
print(cursor.fetchone())
# expected output: (u'foo\x00bar',)
# actual output: (u'foo',)