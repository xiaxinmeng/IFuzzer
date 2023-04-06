name_non_ascii = f'python_test_mmap_ŝƥāɱ_{os.getpid()}'
m = mmap.mmap(-1, 4096, tagname=name_non_ascii)
try:
    _winapi.CloseHandle(_winapi.OpenFileMapping(
        _winapi.FILE_MAP_READ, False, name_non_ascii))
finally:
    m.close()