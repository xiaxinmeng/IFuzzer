class Blah:
	arr = []    # this member should not be 
                    #   shared across all instances of blah
	s = ''

	def __init__(self, s):
		self.s = s

	def __str__( self):
		return '[%s, %s]' % (self.s, str(self.arr))

objs = []
objs.append(Blah('obj-a'))
objs.append(Blah('obj-b'))
objs.append(Blah('obj-c'))