
@functools.total_ordering
class ClassAssignmentCanBreakChecks():
	def __init__(self, i):
		self._i = i
	def __lt__ (self, other):
		last.__class__ = OrdinaryOldInteger
		return self._i < (other._i if hasattr(other, '_i') else other)
@functools.total_ordering
class OrdinaryOldInteger:
	def __init__(self, i):
		self._i = i
	def __lt__(self, other):
		return self._i < (other._i if hasattr(other, '_i') else other)
lst = [ClassAssignmentCanBreakChecks(i) for i in range(10)]
random.shuffle(lst)
last = lst[-1]
lst.sort()
