import subprocess
with subprocess.Popen(("true",), stdin=subprocess.PIPE, bufsize=-1) as p:
    from time import sleep; sleep(1)  # Wait for pipe to be broken
    p.stdin.write(b"buffered data")
