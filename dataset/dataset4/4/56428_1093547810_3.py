import ctypes

commdlg=ctypes.windll.commdlg_plus
commdlg.GetOpenFileNamePlus.argtypes= [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p]
commdlg.GetOpenFileNamePlus.restype= ctypes.c_wchar_p
s=commdlg.GetOpenFileNamePlus(0, "StartDir", "DefFilename", "Text files\0*.txt\0Image files\0*.jpg;*.gif\0\0","txt", "Select a file")