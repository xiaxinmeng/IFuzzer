import modulefinder

with open('import_functools.py', 'w') as f:
   f.write('import functools\n')

mf = modulefinder.ModuleFinder()
mf.run_script('import_functools.py')
print('Test passed')