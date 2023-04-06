class WIN32_FILE_ATTRIBUTE_DATA(ctypes.Structure):
	_fields_ = [("dwFileAttributes", type.DWORD),
	            ("ftCreationTime", type.FILETIME),
	            ("ftLastAccessTime", type.FILETIME),
	            ("ftLastWriteTime", type.FILETIME),
	            ("nFileSizeHigh", type.DWORD),
	            ("nFileSizeLow", type.DWORD)]

GetFileExInfoStandard = 0

wfad = WIN32_FILE_ATTRIBUTE_DATA()