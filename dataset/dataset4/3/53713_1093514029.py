from __future__ import print_function
import os, subprocess, signal

def signal_handler( signum, frame ):

    print( "PID: %s" % pid )
    print( "Timed out! Process %s killed, max exec time (%ss) exceeded" % (pid, timeTol ) )
    os.kill( int( pid ), 15 )
    raise Exception( "Taking too long to finish... aborting!" )

if __name__ == '__main__':

    timeTol = 5

    cmd = 'find /'

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(timeTol)

    p = subprocess.Popen(cmd, shell=True, stderr = subprocess.STDOUT, stdout = subprocess.PIPE)
    pid = p.pid

    out = str( p.communicate()[0].decode() )
    print(out)