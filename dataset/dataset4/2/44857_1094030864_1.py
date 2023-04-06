# Code example:
import turtle, random
from threading import Thread

class Ninja(Thread, turtle.Turtle):
	'A ninja is a threaded turtle'
	
	def __init__(self):
		# constructors
		Thread.__init__(self)
		turtle.Turtle.__init__(self)
		
		# where will i go?
		self.Direction = random.randint(-180,180)
	
	def run(self):
		# that way!
		self.left(self.Direction)
		
		# march 'forward'
		for i in range(50):
			self.forward(16*random.random())
			self.left(22 - 45*random.random())




ninjas = []
for i in range(3):
	ninjas.append(Ninja())
	ninjas[-1].start()