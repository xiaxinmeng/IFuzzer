import os
name = 'sub-fcc'
wrkdir = 'D:\\Bug reports\\Python\\test'
dirname = wrkdir+os.sep+name
print(dirname)
print(ascii(dirname.encode("unicode_internal")))
dirname += os.sep+'bulk'
print(dirname)
print(ascii(dirname.encode("unicode_internal")))