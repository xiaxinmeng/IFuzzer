# if LANC=C then locale.py:getpreferredencoding()->'ANSI_X3.4-1968'
foo= open('setup.py')

# bang! ascii_decode() cannot handle the unicode
bar= foo.read()