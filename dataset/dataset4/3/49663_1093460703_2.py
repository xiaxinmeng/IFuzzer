from ctypes import cdll
from ctypes.util import find_library
sc = cdll.LoadLibrary(find_library("SystemConfiguration"))
x = sc.CFStringCreateWithCString(0, "HTTPEnable", 0)