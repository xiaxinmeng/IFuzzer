def tee(*files):
    return teeIO(*files)


log = file('log.txt', 'w')
err = file('err.txt', 'w')
trace = file('trace.txt', 'w')

sys.stdout = tee(log, sys.__stdout__)
sys.stderr = tee(err, sys.__stderr__)

def write(n, width):
    sys.stdout.write('x' * width)
    if n == 1: return

    write(n - 1, width)
    
try:
    1/0
except:
    write(1, 4096)