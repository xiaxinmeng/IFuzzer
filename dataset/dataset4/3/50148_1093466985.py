from subprocess	import Popen, PIPE
proc1 =	Popen('cat -', shell=True, stdin=PIPE, stdout=PIPE)
proc2 = Popen('cat -', shell=True, stdin=PIPE, stdout=PIPE)
# Removing this line make the proc1.wait() hang
proc2.stdin.close()

proc1.stdin.close()
proc1.wait()