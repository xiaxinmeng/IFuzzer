import io

str_io = io.StringIO('foo bar')
str_io.seek(0, io.SEEK_END)  # seek to end

# Now writes to the stream append instead of overwrite existing characters
str_io.write(' baz')
assert str_io.getvalue() == 'foo bar baz'