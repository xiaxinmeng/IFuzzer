
from ctypes import wintypes, windll, c_void_p, c_size_t, POINTER, c_ubyte, cast
# Define constants.
FILE_MAP_ALL_ACCESS = 983071
PAGE_READWRITE = 4
# Configure function arguments.
windll.kernel32.CreateFileMappingA.argtypes = [wintypes.HANDLE, c_void_p, wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, wintypes.LPCSTR]
windll.kernel32.CreateFileMappingA.restype = wintypes.HANDLE
windll.kernel32.MapViewOfFile.argtypes = [wintypes.HANDLE, wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, c_size_t]
windll.kernel32.MapViewOfFile.restypes = wintypes.LPVOID
# Open shared-memory.
handle = windll.kernel32.CreateFileMappingA(-1, None, PAGE_READWRITE, 0, 1024 * 1024, b'TestSHMEM')
# Obtain pointer to SHMEM buffer.
ptr = windll.kernel32.MapViewOfFile(handle, FILE_MAP_ALL_ACCESS, 0, 0, 1024 * 1024)
arr = cast(ptr, POINTER(c_ubyte))
# or
#arr = POINTER(c_ubyte).from_address(ptr)
arr[0]
# now crashes
