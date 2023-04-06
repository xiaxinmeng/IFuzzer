def evtlt ( self , other ):
	if self.time < other.time:
		return True
	elif self.time == other.time:
		return self.priority < other.priority
	return False

sched.Event.__lt__ = evtlt

def evtgt ( self , other ):
	if self.time > other.time:
		return True
	elif self.time == other.time:
		return self.priority > other.priority
	return False

sched.Event.__gt__ = evtgt