
import pickle

class Child:
	def __init__(self, field):
		self.field = field

class Parent:
	child = Child(0.5)

if __name__ == '__main__':
	i = input()
	if i == 'd':
		parent = Parent()
		parent.child.field = 0.6
		pickle.dump(parent, open('test.pkl', 'wb+'))
	else:
		parent = pickle.load(open('test.pkl', 'rb'))
		print(parent.child.field)
