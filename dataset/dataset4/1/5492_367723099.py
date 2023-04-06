import sys

import tempfile
import multiprocessing

def print_stderr():
    print('stderr:', sys.stderr.fileno(), sys.stderr)
    print('__stderr__:', sys.__stderr__.fileno(), sys.__stderr__)

if __name__ == '__main__':
    sys.stderr = tempfile.TemporaryFile('w')

    p = multiprocessing.Process(target=print_stderr)
    print('Parent:')
    print_stderr()
    print('Child:')
    p.start()
    p.join()