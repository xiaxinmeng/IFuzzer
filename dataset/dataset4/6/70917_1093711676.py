pos = file.tell()  # StringIO position is in code points
file.seek(0)
newfile.write(file.read(pos))
pos = newfile.tell()  # TextIOWrapper position is opaque
newfile.write(file.read())
newfile.seek(pos, 0)