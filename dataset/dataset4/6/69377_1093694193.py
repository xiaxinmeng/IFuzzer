s = StringIO()
print("line", file=s)  # Some inflexible API with an unwanted newline
s.seek(-1, SEEK_CUR)  # Undo the trailing newline
s.truncate()