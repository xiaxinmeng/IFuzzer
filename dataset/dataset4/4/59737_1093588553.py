import subprocess, sys
p = subprocess.Popen(['bash', '-c', 'while true; do echo x; sleep 1; done'], bufsize=0, stdout=subprocess.PIPE)

for line in p.stdout:
    sys.stdout.buffer.write(line)
    sys.stdout.flush()