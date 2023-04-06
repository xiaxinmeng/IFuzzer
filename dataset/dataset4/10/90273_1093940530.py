import subprocess
import os
import sys


def test_small_errpipe_write_fd():
    new_stdout = os.dup(1)
    try:
        os.close(1)
        subprocess.Popen([sys.executable, '-c', "print('AssertionError:0:CLOEXEC failure.')"]).wait()
    finally:
        os.dup2(new_stdout, 0)
        os.dup2(new_stdout, 1)
        test_small_errpipe_write_fd()

test_small_errpipe_write_fd()