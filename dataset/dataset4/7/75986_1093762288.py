from ctypes import cdll, c_int, pointer, Structure
from ctypes.util import find_library
app_services = cdll.LoadLibrary(find_library("ApplicationServices"))
app_services.CGMainDisplayID()