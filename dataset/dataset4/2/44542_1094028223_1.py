cvSetImageROI = _cxDLL.cvSetImageROI
cvSetImageROI.restype = None # void
cvSetImageROI.argtypes = [
    ctypes.c_void_p, # IplImage* image
    CvRect # CvRect rect
    ]