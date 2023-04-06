
if sys.version_info > (2, 4):
    c_py_ssize_t = c_size_t
else:
    c_py_ssize_t = c_int
