from subprocess import *
import sys

p = Popen([sys.executable, "-c", "import sys; print(sys.stdin.read(1))"], stdin=PIPE)
p.stdin.write(b'x')
p.wait()