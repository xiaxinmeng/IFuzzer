
source = b"\xef\xbb\xbf#coding: utf8\nprint('\xe6\x88\x91')\n"

try:
    compile(source, filename="example.py", mode="exec")
except SyntaxError as e:
    print(str(e))
    print(type(e.lineno))
