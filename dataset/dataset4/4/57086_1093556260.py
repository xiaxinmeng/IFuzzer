from subprocess import Popen, PIPE
p = Popen(['ls'], stdout=PIPE)
p.wait()
p.stdout.seek(0)