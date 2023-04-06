import os, shutil
os.makedirs('foo')
os.makedirs('bar/boo')
shutil.move('foo\\', 'bar/')