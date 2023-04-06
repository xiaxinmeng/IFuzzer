import os
import shutil
from distutils import dir_util

shutil.rmtree('folder1')

os.makedirs('folder1/folder2/folder3/')
with open('folder1/folder2/folder3/data.txt', 'w') as fp:
    fp.write('hello')
    
print(os.path.exists('folder1/new_folder2')) # -> prints false
dir_util.copy_tree('folder1/folder2', 'folder1/new_folder2') # -> works

shutil.rmtree('folder1/new_folder2')
print(os.path.exists('folder1/new_folder2')) # -> prints false
dir_util.copy_tree('folder1/folder2', 'folder1/new_folder2') # -> crashes