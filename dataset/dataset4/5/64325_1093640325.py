import sched
import time
import threading

def event( eventNum ):
	print( 'event', eventNum, time.time() )

s = sched.scheduler()
s.enter( 0,1,event, (0,) )
s.enter(10,1,event, (1,) )
t = threading.Thread( target = s.run )
t.start()
s.enter( 5,1,event, (2,) )