reading_lock = threading.Lock ()
readline.set_lock (reading_lock)

def describe (indicator):
	if reading_lock.acquire (False):
		print (indicator.description)
		reading_lock.release ()
	else:
		print ()
		print (indicator.description)
		readline.forced_update_display ()