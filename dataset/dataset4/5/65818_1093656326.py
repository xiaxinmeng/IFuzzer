proc = subprocess.Popen([...], bufsize=support.PIPE_MAX_SIZE * 2,
stdin=subprocess.PIPE, stdout=subprocess.PIPE)
...
proc.stdin.write(b'x' * support.PIPE_MAX_SIZE)