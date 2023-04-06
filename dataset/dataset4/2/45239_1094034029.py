FILENAME = "abc£.bat"
FILENAME.encode ("ascii")
#
# UnicodeEncodeError
#
with open (FILENAME, "w") as f:
  f.write ("echo hello\n")