import shutil
import os

os.mkdir('/dev/shm/t')
os.mkdir('/dev/shm/t/pg')

with open('/dev/shm/t/pg/pol', 'w+') as f:
    f.write('pol')

shutil.copytree('/dev/shm/t/pg', '/dev/shm/t/pg/somevendor/1.0')