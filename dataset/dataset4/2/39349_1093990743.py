from popen2 import Popen3
p1 = Popen3('ls')
p1.fromchild.read()
Popen3('ls').fromchild.read()
Popen3('ls').fromchild.read()
p1.wait()