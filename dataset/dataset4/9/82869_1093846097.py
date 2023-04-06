
import os
import shutil

shutil.rmtree('/tmp/test/', True)
os.makedirs('/tmp/test')
with open('/tmp/test/foo', 'w+') as f:
  f.write('foo')

# now we have /tmp/test/foo, let's simulate what happens in copytree on master

with os.scandir('/tmp/test') as entries:
  # up to this point, /tmp/test/foo is the only entry
  os.makedirs('/tmp/test/1/2/3/', exist_ok=True) # <---- when the iterator starts below in `f in entries`, it will find 1 too
  # now 1 will have been added too
  for f in entries:
    print(f)
