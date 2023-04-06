import os

os.chdir('/tmp')
os.symlink('--success--', 'foo')
print("this should print --success-- :")
print(os.readlink('foo'))
os.unlink('foo')