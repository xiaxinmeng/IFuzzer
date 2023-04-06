class T(ctypes.Structure):
	_fields_ = (
		('member', ctypes.c_char * 16),
	)

x = T()
x.member = bytes('Spam', 'ascii')