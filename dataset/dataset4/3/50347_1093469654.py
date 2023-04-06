import sys
print(repr(sys.argv[1]))
print(repr(sys.argv[1].encode(sys.getfilesystemencoding(),
"surrogateescape")))