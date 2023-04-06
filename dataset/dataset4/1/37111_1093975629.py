import sys
import os
import traceback

if __name__ == '__main__':

    if len(sys.argv) == 1:
        
        try:
            r = os.popen('%s %s %s' % (sys.executable, 
sys.argv[0], -1,))
            r.close()
        except IOError:
            traceback.print_exc()