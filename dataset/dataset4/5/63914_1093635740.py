import ctypes
def do_test(t):
    h = ctypes.windll.kernel32.CreateFileW("test.txt", 0xC0000000, 7, None, 2, 0, 0)
    assert h != -1
    try:
        mt1 = ctypes.c_uint64(t)
        assert ctypes.windll.kernel32.SetFileTime(h, None, None, ctypes.byref(mt1)) != 0
        mt2 = ctypes.c_uint64()
        assert ctypes.windll.kernel32.GetFileTime(h, None, None, ctypes.byref(mt2)) != 0
        assert mt1.value == mt2.value
        print(mt2.value)
    finally:
        assert ctypes.windll.kernel32.CloseHandle(h) != 0