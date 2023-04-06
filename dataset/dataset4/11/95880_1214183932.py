
f = io.StringIO('first line\n')
f.seek(0, io.SEEK_END)
f.write('second line\n')
print(f.getvalue())
