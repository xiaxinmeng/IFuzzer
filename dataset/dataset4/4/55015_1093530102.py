import os, subprocess, sys

x=os.open('/dev/null', os.O_RDWR)
os.close(0)
os.close(1)
os.close(2)

res = subprocess.Popen([sys.executable, "-c",
                      'import sys;'
                      'sys.stdout.write("apple");'
                      'sys.stdout.flush();'
                      'sys.stderr.write("orange")'],
           stdin=x,
           stdout=subprocess.PIPE,
           stderr=subprocess.PIPE).communicate()
with open('/tmp/out', 'w') as f:
    f.write(repr(res) + '\n')
    f.write(repr((b'apple', b'orange')) + '\n')