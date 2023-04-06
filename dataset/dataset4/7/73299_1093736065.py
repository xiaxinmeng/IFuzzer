from modulefinder import ModuleFinder

finder = ModuleFinder()
finder.run_script('test.py')

print('Loaded modules:')
for name, mod in finder.modules.items():
    print('%s: ' % name, end='')
    print(','.join(list(mod.globalnames.keys())[:3]))