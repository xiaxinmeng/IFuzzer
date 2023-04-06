fd = os.dup(sys.stdout.fileno())
subprocess.call([sys.executable, '-c',
                 'import sys;'
                 'print("Hello stdout");'
                 'print("Hello fd", file=open(int(sys.argv[1]), "w"))',
                 str(fd)],
                stdout=fd,
                pass_fds=[fd])