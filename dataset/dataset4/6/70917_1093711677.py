pos = file.tell()
tail = file.read()
file.seek(0)
head = file.read()
if tail:
    head = head[:-len(tail)]
newfile.write(head)
pos = newfile.tell()  # TextIOWrapper position is opaque
newfile.write(tail)
newfile.seek(pos, 0)