#######
import os

os.mkdir('path1')
os.mkdir('path1/package')
with open('path1/package/mod.py', 'w') as fp:
    fp.write('print(42)\n')

import site
site.addsitedir('path1')
import package.mod