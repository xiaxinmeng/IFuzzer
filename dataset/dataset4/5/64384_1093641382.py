class slice_index_converter(CConverter):
    type = 'Py_ssize_t'
    converter = '_PyEval_SliceIndex'