# Python 3.1.2rc1 (r312rc1:78742, Mar  7 2010, 07:49:40)
# [MSC v.1500 32 bit (Intel)] on win32
import ctypes

class T(ctypes.Structure):
	_fields_ = (
		('member', ctypes.c_char * 16),
	)