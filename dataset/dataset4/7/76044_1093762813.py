import multiprocessing
import os
import signal
import subprocess
import sys
import time

def kill_with_os_kill(proc):
    print('kill with os.kill(pid,SIGTERM)')
    os.kill(proc.pid, signal.SIGTERM)

def kill_with_terminate(proc):
    print('kill child with proc.terminate()')
    proc.terminate()

def run_and_kill_subprocess(killfn, procarg):
    print('run subprocess child with %s' % procarg)
    with subprocess.Popen([sys.executable, __file__, procarg]) as proc:
        time.sleep(1)
        killfn(proc)
        proc.wait()
    print('child terminated with %s' % proc.returncode)

def run_and_kill_multiprocessing(killfn, procarg):
    print('run multiprocessing child with %s' % procarg)
    proc = multiprocessing.Process(target=childmain, args=(procarg,))
    proc.start()
    time.sleep(1)
    killfn(proc)
    proc.join()
    print('child terminated with %s' % proc.exitcode)

def childmain(arg):
    print('child process started with %s' % arg)
    while True:
        pass

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('parent process started')
        run_and_kill_subprocess(kill_with_os_kill, 'subprocess-oskill')
        run_and_kill_subprocess(kill_with_terminate, 'subprocess-terminate')
        run_and_kill_multiprocessing(kill_with_os_kill, 'multiprocessing-oskill')
        run_and_kill_multiprocessing(kill_with_terminate, 'multiprocessing-terminate')
    else:
        childmain(sys.argv[1])