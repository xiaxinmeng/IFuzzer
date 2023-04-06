def work(t):
    sleep(t)

twork = 3; twait = 4
t = Thread(target=work, args=(twork,))
try:
	t.start()
	t.join(twait)  # here I do Ctrl-C
except KeyboardInterrupt:
	pass
t.join()  # this hangs if twork < twait