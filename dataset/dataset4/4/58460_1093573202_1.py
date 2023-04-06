from subprocess import *
import sys, time

p = Popen([sys.executable, '-c', '''
import time, sys
for i in range(3): 
    time.sleep(.3)
    print '.',
    sys.stdout.flush()
print 'exiting'
'''], stdout = sys.stdout, stderr = sys.stderr)