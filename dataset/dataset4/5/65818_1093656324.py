proc = subprocess.Popen([...], bufsize=support.PIPE_MAX_SIZE, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
proc.stdout.read()  # Make sure subprocess has closed its input
proc.stdin.write(bytes(support.PIPE_MAX_SIZE))
self.assertIsNone(proc.returncode)
# Expect EPIPE under POSIX and EINVAL under Windows
self.assertRaises(OSError, proc.__exit__, None, None, None)