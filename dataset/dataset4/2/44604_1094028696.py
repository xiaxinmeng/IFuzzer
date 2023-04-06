import inspect,sys

print('Version info:',sys.version_info)
print()

f1 = inspect.getabsfile(inspect)
f2 = inspect.getabsfile(inspect.iscode)
print('File for `inspect`       :',f1)
print('File for `inspect.iscode`:',f2)
print('Do these match?',f1==f2)
if f1==f2:
    print('OK')
else:
    print('BUG - this is a bug in this version of Python')