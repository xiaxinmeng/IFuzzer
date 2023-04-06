def print3(*args, end='\r'):
    sys.stdout.write(' '.join(*args))
    sys.stdout.write(end)
    sys.stdout.flush()