import sys
f = open("stderr.txt", "w")
f.write("stdin: %i\n" % sys.stdin.fileno())
f.write("stdout: %i\n" % sys.stdout.fileno())
f.write("stderr: %i\n" % sys.stderr.fileno())